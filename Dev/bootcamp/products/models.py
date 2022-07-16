from django.db import models, IntegrityError, DataError
from django.core.exceptions import ValidationError
from manufacturer.models import Manufacturer
from django.http.response import Http404
from accounts.models import CustomUser
from .storages import ProtectedStorage
from django.utils.translation import gettext as _
from bootcamp.settings import LOGGER
from django.urls import (
    reverse,
    reverse_lazy
)


# Create your models here.
class Product(models.Model):
    '''
    ===========================================================
    This class represents the product object outlined in the db
    ===========================================================
    Attrs:
        :param id: = models.AutoField()
        :param title: Describes the products title
        :type title: str, max_length = 220
        :param content: product description
        :type content: str, not compulsory
        :param price: price of the product
        :type price: int
        :manufacturers: reflects definition of "many-to-many" relationship
        :type manufacturers: 'many-to-many' field
        :param image: restricted to image formats only
        :type image: files.ImageFieldFile
        :param media: restricted to file formats compliant with db
        :type media: files.FieldFile

    .. note::
        multiple records in the Product table are associated with multiple
        records in the Manufacturer tablerer

        :Example:
        products.manufacturer.get(id=1) --> manufacturer1
        products.manufacturer.all() --> <QuerySet [Product(id=1),
                                        Product(id=5) ...]>
    '''

    # id = models.AutoField()
    title = models.CharField(max_length=220)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, default=0)
    # in case user was deleted sets it's value as null in the db
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    manufacturers = models.ManyToManyField(
        Manufacturer,
        related_name='products'
    )
    image = models.ImageField(
        upload_to='media/products/',
        null=True,
        blank=True
    )
    media = models.FileField(
        storage=ProtectedStorage,
        upload_to='protected/products/',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        '''
        Magic method aims to show basic info about a Product
        :returns: product name and price

        ..note:
            price is null only when hardcoded from postgres
        '''
        if_price = 0
        if self.price is not None:
            if_price = lambda price: f': {str(self.price)}$'
        return f'{self.title}' + if_price(self.price)

    def __repr__(self):
        '''
        This magic method is redefined to show class and id of a product object.
        :returns: class, id
        '''
        return f'{self.__class__.__name__}(id={self.id})'

    @property
    def owner(self):
        return self.user

    def get_image_url(self):
        if self.image:
            return u'%s' % self.image.url
            # return u'<img src="%s" width="50" height="50"/>' % self.image.url
        return u'image wasn\'t found'

    def get_absolute_url(self):
        '''
        redefine parental method with an object url quick access
        feature to our model “View on site” link in the admin app.
        jumps directly to the object’s public view, as given by
        get_absolute_url()

        :returns: product object cannonical url

        ..note:: reverse_lazy is useful because it prevent
                Reverse Not Found exceptions when working
                with URLs that may not be immediately known

                object cannonical url <str> type when reverse
                <django.utils.functional.lazy.<locals>.__proxy__>

        '''
        return reverse_lazy(
            'products:detailed_view',
            kwargs={'product_id': self.pk}
        )

    @staticmethod
    def get_by_id(product_id):
        '''
        :param product_id: SERIAL: the id of a Product to be found in the DB
        :returns: product object or None if a product with such ID does not exist
        '''
        try:
            product = Product.objects.get(pk=product_id)
            return product
        except Product.DoesNotExist:
            LOGGER.warning("Item does not exist")
            raise Http404(_('Item wasn\'t found'))

    @staticmethod
    def get_all():
        '''
        :returns: data for json request with QuerySet of all products
        use iteration to render separately in a template
        '''
        try:
            all_products = Product.objects.all()
            return list(all_products)
        except (IndexError, TypeError, Product.DoesNotExist):
            message = 'So far no items availbale'
            LOGGER.info(message)
            raise Http404(_(message))

    @staticmethod
    def create(title, content, price, user=None,
               manufacturers=None, image=None, media=None):
        '''
        :param name: Describes name of the product
        :type name: str max_length=220
        :param content: Describes description of the book
        :type description: str
        :param price: Describes a price of a product
        :type price: int default=10

        :returns: a new product object which is also written into the DB
        '''
        # allows to create objects with not all attrs input obligatory
        product = Product(
            title=title, content=content,
            price=price, user=user,
            image=image, media=media
            )
        try:
            product.save()
            manufacturer_exists = manufacturers is not None
            if manufacturer_exists:
                for manufacturer in manufacturers:
                    product.manufacturers.add(manufacturer)
            product.save()
            return product
        except (IntegrityError, AttributeError, DataError, ValueError):
            LOGGER.warning('Wrong attributes or relational integrity error')
            raise ValidationError(_('Check if field entries r correct'))

    def update(self, **kwargs):
        '''
        Updates product in the database with the specified parameters.\n
        :param title: Depicts product title of a product
        :type title: str max_length=128
        :param content: Depicts description of a product
        :type content: str
        :param price: shows a product's price
        :type price: int default=10
        :returns: updated model object
        '''
        self.__dict__.update(**kwargs)
        self.save()
        return self

    def to_dict(self):
        '''
        removes id & db _state
        :returns: product title, content, price
        :Example:
        | {
        |   'title': 'Raspberry Pi',
        |   'content': 'some content',
        |   'price': 'some price'
        | }
        '''
        data = dict()
        if self.title:
            data.update(title=self.title)
        if self.content:
            data.update(content=self.content)
        if self.price:
            data.update(price=self.price)
        if self.user:
            data.update(user=self.user)
        if self.manufacturers:
            data.update(manufacturers=self.manufacturers)
        if self.image:
            data.update(image=self.image)
        if self.media:
            data.update(media=self.media)
        return data

        # index = 2
        # keys = list(self.__dict__.keys())[index:]
        # values = list(self.__dict__.values())[index:]
        # api_data = dict(zip(keys, values))
        # return api_data

    @staticmethod
    def delete_by_id(product_id):
        '''
        :param product_id: an id of a product to be deleted
        :type product_id: int
        :returns: True if the object existed in the db and was
        :exception will be trown automatically
        from previous method when no item in db
        '''
        product = Product.get_by_id(product_id)
        product.delete()
        return True

    @staticmethod
    def update_by_id(product_id, data=None):
        '''
        This method is created in order to update product object
        :params: same as in create method, if param is None - no update done
        :returns: None
        '''
        try:
            product = Product.get_by_id(product_id)
            product.__dict__.update(data)
            product.save()
            return product

        except (IntegrityError, AttributeError, DataError, ValueError) as err:
            LOGGER.error(f'{err}')
            raise ValidationError(_('Check if field entries r correct'))
