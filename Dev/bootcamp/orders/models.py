from django.core.exceptions import ValidationError
from django.db.utils import InterfaceError
from django.utils.translation import gettext as _
from django.db import models, DataError, IntegrityError

import datetime

from django.http.response import Http404, HttpResponse
from products.models import Product
from accounts.models import CustomUser
import time, datetime
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib import messages
from bootcamp.settings import (
    LOGGER,
    # DEBUG # remove after 
)
    # Create your models here.
class Order(models.Model):
        
    '''
    This class represents the order that'll be added to a cart
    
    Args:
        :param 'product': Outlines the product that will be added to a cart
        :type 'product': Foreign Key - constraint that references to a primary
            key of Product.id fields
        :param 'created_at': outlines the creation date of a product
        :type 'created_at': datetime field
        :param user: outlines the user that is adding a product to a cart
        :type 'product': Foreign Key - constraint that references to a primary
        key of User.id fields

    ..note:: logging here is implement via
            catching errors db errors and
            raisisng Http errors with 'str'
            custom message
    '''

    #id is the autofield
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)

    # 1
    def __str__(self):
        '''
        Magic method aims to show basic info about the order object
        :returns: order id, converted creted time & user if such exists
        '''
        is_user = lambda user: f'-{self.user}' if self.user != None else ''
        convert_time = lambda created_at: f'-{self.created_at.strftime("%d/%m/%Y")}' if True else ''
        return f'Order№{self.id} ({self.product}' + \
                    convert_time(self.created_at) + \
                    is_user(self.user) +')'

    # 2
    def __repr__(self):
        '''
        This magic method is redefined to show class name and id
        :returns: class, id
        '''
        return f'{self.__class__.__name__}(id={self.id})'

    #3 
    def get_absolute_url(self, *args):
        '''
        redefines the model's class with an object-editing page 
        feature: “View on site” link in the admin app.
        jump directly to the object’s public view, as given by
        get_absolute_url()
        :returns: user's cart identified by user_id
        '''
        if self.user is None:
            message = f'User\'s cart wasn\'t found'
            print(message)
            LOGGER.warning(message)
            raise Http404(message)
        return reverse_lazy(
            'orders:cart_view',
            args=[str(self.user.id)]
            )

    # 4
    @staticmethod
    def create(product):
        '''
        This magic method is redefined to create order based on particular product 
        and saved to db
        :returns: order object
        '''
        order = Order(product=product)
        try:
            order.save()
            return order
        except (IntegrityError, AttributeError, DataError, ValueError):
            LOGGER.warning('Wrong attributes or relational integrity error')
            pass

    # 5
    @staticmethod
    def get_all(user_id=None):
        '''
        This method gets all orders from the db
        return: queryset of product objects converted
        to a list
        '''
        condition = len([
            product for product in Product.get_all()
            ]) > 0
        return [
            order for order in Order.objects.all()
            ] if condition else list()

    # 6
    @staticmethod
    def get_by_id(order_id):
        '''
        :param order_id: SERIAL: the id of an Order to be found in the DB
        returns: product object or None if the order with such ID does not exist
        '''
        try:
            order = Order.objects.get(pk=order_id)
            return order
        except Order.DoesNotExist:
            message = f'Order does not exist'
            LOGGER.warning(message)
            raise Http404(_(message))
            
    # 7
    @staticmethod
    def delete_by_id(order_id):
        '''
        :param user_id: SERIAL: id of the authenticated user
        return: delete all objects found in the db (clean the db)
        '''
        try:
            order = Order.objects.get(pk=order_id)
            order.delete()
            return True
        except Order.DoesNotExist:
            message = 'Order does not exist'
            LOGGER.warning(message)
            raise Http404(_(message))
        #     pass
        # return False

    # 8
    @staticmethod
    def delete_all(user_id=None):
        '''
        :param user_id: SERIAL: the id of an Order to be found in the DB
        return: delete all objects found in the db (clean the db)
        '''
        product_exist = len([
            product for product in Product.get_all()
            ]) > 0
        order_exist = len([
            order for order in Order.get_all()
            ]) > 0

        if product_exist and order_exist:
            return Order.objects.all().filter(user_id=user_id).delete()
        message = f'No orders or products so far'
        LOGGER.warning(message)
        raise Http404(_('No orders or products so far'))

    # 9
    @staticmethod
    def get_orders_by_user(user_id=None):
        '''
        :returns: empty qs of orders by user
            empty qs when user does not exist
        ..note:: We can attach ip condition here for later
            for anonymous users, to have several of them
            and allow them to create cart
        '''
        return Order.objects.all().filter(user_id=user_id)

    ## *** CART FUNCTIONALITY *** ##
    # 10
    @staticmethod
    def create_cart(user_id=None):
        
        products = [order.product.title for order in Order.get_orders_by_user(user_id)] ### +++
        orders = Order.get_orders_by_user(user_id) ### +++
        zipped = dict(zip(products, orders))

        ## form empty basket: key - order, value - list of products
        basket = {}
        for i in range(len(zipped)):
            basket[list(zipped.values())[i]] = []

        ## fill the dict-type basket
        try:
            for i in range(len(products)):
                iteration = i <= len(basket) - 1
                for product in products if iteration else 0: ### +++
                    similar_product = product == list(basket.keys())[i].product.title
                    list(basket.values())[i].append(product) if similar_product else 0 ### +++
        except TypeError as err:
            LOGGER.error(f'{err}')
            pass
        return basket
    
    # 11
    @staticmethod
    def cart_items_amount(user_id=None):  ## add user_id late
        basket = Order.create_cart(user_id)
        #products_amount = 0
        for order, products in basket.items():
            basket[order] = len(products)
            #products_amount += len(products)
        
        return basket

    # 12
    @staticmethod
    def products_amount(user_id=None):
        basket = Order.cart_items_amount(user_id)
        return sum(list(basket.values()))
        
    # 13
    @staticmethod
    def total_value(user_id=None):
        try:
            total_value = float(sum([
                order.product.price for order in Order.get_orders_by_user(user_id)
                ]))
            return total_value
        except (IntegrityError, AttributeError, DataError, ValueError):
            LOGGER.warning(_('Check if price entries r digits'))
            raise ValidationError(_('Check if price entries r digits'))
    
    # 14
    @staticmethod
    def get_discount(user_id=None):
        products_amount = Order.products_amount(user_id)
        disc_ratio = ((products_amount//5)*5)/100
        max_disc = int(disc_ratio*100) not in range(0, 50)
                    
        disc_ratio = disc_ratio if not max_disc else 0.5
        return disc_ratio
    
    # *** RECEIPT ADDITIONAL FUNCTIONALITY *** #
    # 14
    def get_value_per_amount(self, user_id=None):
        ''' 
        instantiate form Order class to use this method
        param user_id: SERIAL: the id of an Order to be found in the DB
        returns: total amount per single item 
        '''
        basket = Order.cart_items_amount(user_id)
        amounts = [k.product.price * v  for k, v in basket.items()]
        for i in range(len(amounts)):
            list(basket.keys())[i].amounts = amounts[i]
        return basket
    
    # 15
    def calculate_shipping(self, user_id=None):
        ''' 
        ..note:: elaborate shipping formula aforehand (company policy)

            param user_id: SERIAL: the id of an Order to be found in the DB
            returns: shipping price for cart
            size (volume, l): k1
            weight (kg): k2
            route (km): k3
        '''
        try:
            products_amount = Order.products_amount(user_id)
            pass
        except (DataError, TypeError, ValueError):
            raise ValidationError(_('Check if field entries r correct'))
