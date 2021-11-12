from django.conf.urls import include
from django.urls import path, re_path
from orders.views import (
    order_create_view,
    cart_view,
    order_remove_view,
    cart_clean_view,
    process_payment_view,
    api_process_payment_view,
    PaypalReturnView,
    PaypalCancelView,
    PaypalFormView,
    payment_complete_view
)

from django.conf import settings
from django.views.generic import TemplateView, ListView # Import TemplateView


app_name = 'orders'

urlpatterns = [
    
    re_path(r'order/cart/', cart_view, name='cart_view'),

    # ############# *** DeatailedView + API *** ###############
    #re_path(r'^order/(?P<order_id>\d+)/$', order_detailed_view, name='detailed_view'),
    # re_path(r'^api/manufacturers/(?P<manufacturer_id>\d+)/$', api_manufacturer_detailed_view, name='api_detailed_view'),

    ################ *** Create View *** #################
    re_path(r'^order/create/(?P<product_id>\d+)/$', order_create_view, name='order_create_view'),

    ################ *** Delete View *** #################
    re_path(r'^order/delete/(?P<order_id>\d+)/$', order_remove_view, name='order_remove_view'),

    # ############# *** Clean the Cart View *** ###############
    re_path(r'^order/clean-cart/$', cart_clean_view, name='cart_clean_view'),

    # ############# *** Order Pay View *** ###############
    ## set 1 
    re_path(r'^order/payment/$', process_payment_view, name='process_payment_view'),
    re_path(r'^api/order/payment/$', api_process_payment_view, name='api_process_payment_view'),

    # re_path(r'^order/payment-done/$', TemplateView.as_view(template_name="orders/payment_done.html"), name='payment_done'),
    # re_path(r'^order/payment-canceled/$', TemplateView.as_view(template_name="orders/payment_canceled.html"), name='payment_canceled'),

    ## set 2
    # ############# *** Order Pay View *** ###############
    path('paypal-payment/', PaypalFormView.as_view(), name='paypal-payment'),
    path('paypal-done/', payment_complete_view, name='paypal-done'),
    path('paypal-return/', PaypalReturnView.as_view(), name='paypal-return'),
    path('paypal-cancelled/', PaypalCancelView.as_view(), name='paypal-cancel'),
    
]