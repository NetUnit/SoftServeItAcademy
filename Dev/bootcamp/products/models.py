from django.db import models, IntegrityError, DataError
from manufacturer.models import Manufacturer
from django.http.response import Http404

# Create your models here.
class Product(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=220)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    manufacturers = models.ManyToManyField(Manufacturer, related_name='products')

    class Meta:
        ordering = ('id',)

    # def __str__(self):
    #     """
    #     Magic method is redefined to show all information about a Product
    #     :return: product id, product title, product title, product price
    #     """
    #     # return f'{self.id} {self.title} {self.price} {self.manufacturers}'
    #     # return str(self.to_dict())[1:-1]

    def __repr__(self):
        """
            This magic method is redefined to show class and id of product object.
            :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(product_id):
        """
            param product_id: SERIAL: the id of a Product to be found in the DB
            return: product object or None if a product with such ID does not exist
        """
        try:
            product = Product.objects.get(pk=product_id)
            return product
        except Product.DoesNotExist:
            raise Http404
            # LOGGER.error("Product does not exist")

    @staticmethod
    def get_all():
        """
            returns data for json request with QuerySet of all books
            use iteration to render separately in a template
        """
        try:
            all_products = Product.objects.all()
            return list(all_products)
        except (IndexError, TypeError, Product.DoesNotExist):
            pass
        return False

    @staticmethod
    def create(title, content, price, manufacturers=None):
        """
            param name: Describes name of the product
            type name: str max_length=220
            param content: Describes description of the book
            type description: str
            param price: Describes a price of a product
            type price: int default=10

            :return: a new product object which is also written into the DB
        """
        # allows to create objects with not all attrs input obligatory
        product = Product(title=title, content=content, price=price)
        try:
            product.save()
            manufacturer_exists = manufacturers is not None
            if manufacturer_exists:
                for manufacturer in manufacturers:
                    product.manufacturers.add(manufacturer)
            product.save()
            return product
        except (IntegrityError, AttributeError, DataError):
            # LOGGER.error("Wrong attributes or relational integrity error")
            pass
        
    
    def update(self, title=None, content=None, price=None):
        """
            Updates product in the database with the specified parameters.\n
            param title: Depicts product title of a product
            type title: str max_length=128
            param content: Depicts description of a product
            type content: str
            param price: shows a product's price
            type cprice: int default=10
            :return: None
        """
        if title:
            self.title = title
        if content:
            self.content = content
        if price:
            self.price = price
        self.save()

    @staticmethod
    def delete_by_id(product_id):
        """
            :param product_id: an id of a product to be deleted
            :type product_id: int
            :return: True if the object existed in the db and was removed or False if it didn't exist
        """

        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            return True
        except Product.DoesNotExist:
            # LOGGER.error("User does not exist"
            pass
        return False

## update
    # >>> setattr(prod, 'content', 'cool thing')
    # >>> prod.save()