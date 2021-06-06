from django.db import models, IntegrityError, DataError

# Create your models here.
class Product(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=220)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)

    # class Meta:
    #     ordering = ('id',)

    # def __str__(self):
    #     """
    #     Magic method is redefined to show all information about a Product
    #     :return: product id, product title, product title, product price
    #     """
    #     return str(self.to_dict())[1:-1]

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
    
    @staticmethod
    def create(title, content, price):
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
            return product
        except (IntegrityError, AttributeError, DataError):
            # LOGGER.error("Wrong attributes or relational integrity error")
            pass
    
    @staticmethod
    def delete_by_id(product_id):
        """
            :param book_id: an id of a book to be deleted
            :type book_id: int
            :return: True if object existed in the db and was removed or False if it didn't exist
        """

        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            return True
        except Product.DoesNotExist:
            # LOGGER.error("User does not exist"
            pass
        return False
        
