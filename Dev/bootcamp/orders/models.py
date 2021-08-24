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

    '2 Scope of Dajngo: Fat Models, Helper Modules, Thin Views, Stupid Templates'



    '''

    #id is the autofield
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


    # def __str__(self):
    #     '''
    #     Magic method is redefined to show all information about an order
    #     :return: order id, created at, user_id, product_id
    #     '''
    #     return f'----{self.product}{self.created_at}' ## {self.user}


    def __repr__(self):
        '''
        This magic method is redefined to show class and id of the Order object.
        :return: class, id
        '''
        return f'{self.__class__.__name__}(id={self.id})'


    @staticmethod
    def create(product):
        '''
        This magic method is redefined to create order based on particular product 
        and saved to db
        :return: order object
        '''
        order = Order(product=product)
        try:
            order.save()
            return order
        except (IntegrityError, AttributeError, DataError, ValueError):
            # LOGGER.error("Wrong attributes or relational integrity error")
            pass
    

    @staticmethod
    def get_all():
        '''
            This method gets all orders from the db
            return: queryset of product objects converted to a list
        '''
        condition = len([
            product for product in Product.get_all()
            ]) > 0
        return [
            order for order in Order.objects.all()
            ] if condition else 0


    @staticmethod
    def get_by_id(order_id):
        '''
            param order_id: SERIAL: the id of an Order to be found in the DB
            return: product object or None if the order with such ID does not exist
        '''
        try:
            order = Order.objects.get(pk=order_id)
            return order
        except Order.DoesNotExist:
            # LOGGER.error("User does not exist")
            pass
        return False


    @staticmethod
    def delete_by_id(order_id):
        '''
            param user_id: SERIAL: the id of an authenticated user
            return: delete all objects found in the db (clean the db)
        '''
        try:
            order = Order.objects.get(pk=order_id)
            order.delete()
            return True
        except Order.DoesNotExist:
            # LOGGER.error("User does not exist")
            pass
        return False


    @staticmethod
    def delete_all():
        '''
            param user_id: SERIAL: the id of an Order to be found in the DB
            return: delete all objects found in the db (clean the db)
        '''
        product_exist = len([
            product for product in Product.get_all()
            ]) > 0
        order_exist = len([
            order for order in Order.get_all()
            ]) > 0

        if product_exist and order_exist:
            return Order.objects.all().delete()

    @staticmethod
    def create_cart():  ## add user_id later

        products = [order.product.title for order in Order.get_all()]
        orders = Order.get_all()
        zipped = dict(zip(products, orders))

        ## form empty basket: key - order, value - list of products
        basket = {}
        for i in range(len(zipped)):
            basket[list(zipped.values())[i]] = []

        ## fill the dict-type basket
        try:
            for i in range(len(products)):
                iteration = i <= len(basket) - 1
                for product in products if iteration else 0:
                    similar_product = product == list(basket.keys())[i].product.title
                    list(basket.values())[i].append(product) if similar_product else 0
        except TypeError as err:
            # LOGGER.error(f'{err}')
            pass
        
        return basket
    
    @staticmethod
    def cart_items_amount():  ## add user_id late
        basket = Order.create_cart()
        #products_amount = 0
        for order, products in basket.items():
            basket[order] = len(products)
            #products_amount += len(products)
        
        return basket


    @staticmethod
    def total_amount():  ## add user_id late
        basket = Order.cart_items_amount()
        return sum(list(basket.values()))
        




        # return Order.objects.all().filter(id=user_id).delete() if condition else 0 # for user_id - when having a user

    

    # add calculate basket here
    ## 1) calculate number of items
    ## 2) calculate discount
    ## 3) calculate total nember of items
    ## !!! get all of these things from basket views
   