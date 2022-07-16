from django.db import models, IntegrityError, DataError
from django.forms.models import model_to_dict
from django.http.response import Http404
from products.storages import ProtectedStorage
from django.urls.base import reverse_lazy
from bootcamp.settings import LOGGER
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


# Create your models here
class Manufacturer(models.Model):

    '''
    ===========================================================
    This class represents the manufacturer of a certain product
    ===========================================================
    Attrs:
        :param id: = models.AutoField()
        :param name: Describes the comapny name
        :type name: str max_length = 40
        :param country: Depicts the manufacturer's country of origin
        :type country: str max_length = 20
        :param year: depicts the foundation year year of a company
        :type year: 'datetime.date'

    .. note::
        Manufacturer is associated through many-to-many relationship
        with Product

        :Example:
        manufacturer.products.get(id=1) --> product1
        manufacturer.products.all() --> manufacturer1
    '''

    title = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=20, blank=True)
    year = models.DateField()
    image = models.ImageField(
        upload_to='media/manufacturers/',
        null=True,
        blank=True
    )
    media = models.FileField(
        storage=ProtectedStorage,
        upload_to='protected/manufacturers/',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        '''
        Magic method aims to show basic info about a manufacturer
        :returns: manufacturer.title,  manufacturer.country,  manufacturer.year

        '''
        return f'{self.title} LTD'

    def __repr__(self):
        '''
        This megic method is redefined in order to show class name and id
        of a certain product object
        :returns: class, id
        '''
        return f'{self.__class__.__name__}(id={self.id})'

    def get_absolute_url(self):
        return reverse_lazy(
            'manufacturer:get_products_manufacturer',
            args=[str(self.id)]
        )

    @staticmethod
    def get_by_id(manufacturer_id):
        '''
        This method is created in order to get manufacturers object
        found in the DB
        :returns: Manufacturer object or None if such a manufacturer
        does not exist in the DB (None will raise 404 status)
        '''
        try:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
            return manufacturer
        except Manufacturer.DoesNotExist as err:
            LOGGER.warning(f'{err}')
            raise Http404(_('Manufacturer wasn\'t found'))

    @staticmethod
    def get_all():
        '''
        This method is created in order to get a queryset of all present
        objects found in the db
        :returns: Manufacturer queryset of all objects or empty list if
        nothing has been found in the db
        '''
        try:
            manufacturers = Manufacturer.objects.all()
            return list(manufacturers)
        except Manufacturer.DoesNotExist as err:
            LOGGER.error(f'{err}')
            raise Http404(_('So far no manufacturer\'s added'))

    @staticmethod
    def delete_by_id(manufacturer_id):
        '''
        This method is created in order to delete manufacturer object
        found in the DB
        :returns: True if such an object was found in the DB or False
        if it didn't existed
        '''
        manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
        manufacturer.delete()
        return True

    @staticmethod
    def create(title, country, year, image, media):
        '''
        This method is created in order to create manufacturer object
        to be saved into a DB
        :param name: Describes the comapny name
        :type: str max_length = 40
        :param country: Depicts the manufacturer's country of origin
        :type: str max_length = 20
        :param year: depicts the foundation year of a company
        :type date: datetime autofiled
        :param image: input field for upload/download of images
        :type image: files.ImageFieldFile
        :param file: input field for upload/download of files
        :type file: files.FieldFile
        '''
        try:
            manufacturer = Manufacturer.objects.create(
                title=title, country=country, year=year,
                image=image, media=media
            )
            manufacturer.save()
            return manufacturer
        except(IntegrityError, DataError, AttributeError, ValueError):
            LOGGER.warning('Wrong attributes or relational integrity error')
            raise ValidationError(_('Check if field entries r correct'))

    def update(self, **kwargs):
        '''
        :params: data - comes from the form - dict ({key: value})
        number/presence of user keyword parameters doesn't matter
        :returns: updated object or None
        '''
        self.__dict__.update(**kwargs)
        self.save()
        return self

    @staticmethod
    def update_by_id(manufacturer_id, title=None,
                     country=None, year=None,
                     image=None, media=None):
        '''
        This method is created in order to update manufacturer object
        :params: same as in create method, if param is None - no update done
        :returns: updated object or None
        '''
        try:
            manufacturer = Manufacturer.get_by_id(
                manufacturer_id
            )
            update_data = {
                    'title': title,
                    'country': country,
                    'year': year,
                    'image': image,
                    'media': media
                    }
            manufacturer.__dict__.update(**update_data)
            manufacturer.save()
            return manufacturer

        except (IntegrityError, AttributeError, DataError, ValueError) as err:
            LOGGER.error(f'{err}')
            raise ValidationError(_('Check if field entries r correct'))

    @staticmethod
    def get_products_manufacturer(manufacturer_id):
        manufacturer = Manufacturer.get_by_id(manufacturer_id)
        products = Product.objects.all().filter(
            manufacturer=manufacturer
        )
        # alternatively the same result using 'many-to-many' relationship
        # products = manufacturer.products.all()
        return products
