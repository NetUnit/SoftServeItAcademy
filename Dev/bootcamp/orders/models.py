from django.db import models, DataError, IntegrityError

import datetime
from products.models import Product
from manufacturer.models import Manufacturer

# Create your models here.
class Order(models.Model):
        
    '''
    This class represents the order that'll be added to a cart \n
    -----------------------------------------------------------
    Attrs:
    param 'product': Outlines the product that will be added to a cart
    type: Foreign Key - constraint that references to a primary key of Product.id fields
    param 'created_at': outlines the creation date of a product
    type: datetime field
    param user: outlines the user that is adding a product to a cart
    type: Foreign Key - constraint that references to a primary key of User.id fields

    NOTE: Manufacturer model is more customized than Product
          in order to avoid less code in views
    '''
    #id is the autofield
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        '''
        Magic method is redefined to show all information about an order
        :return: order id, created at, user_id, product_id
        '''
        return f'{self.id}{self.product}{self.created_at}' ## {self.user}

    def __repr__(self):
        '''
        This magic method is redefined to show class and id of the Order object.
        :return: class, id
        '''
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def create(product):
        order = Order(product=product)
        try:
            order.save()
            return order
        except (IntegrityError, AttributeError, DataError, ValueError):
            # LOGGER.error("Wrong attributes or relational integrity error")
            pass
