from django.conf.urls import include
from django.urls import path, re_path
from orders.views import (
    order_create_view,
    cart_view,
    order_remove_view,
    cart_clean_view,

)

from django.conf import settings

app_name = 'orders'

urlpatterns = [
    
    re_path(r'order/cart/', cart_view, name='cart_view'),

    # ############# *** OrderDeatailedView + API *** ###############
    #re_path(r'^order/(?P<order_id>\d+)/$', order_detailed_view, name='detailed_view'),
    # re_path(r'^api/manufacturers/(?P<manufacturer_id>\d+)/$', api_manufacturer_detailed_view, name='api_detailed_view'),

    # ############# *** ManufacturerListView *** ###############
    # re_path(r'^manufacturers/list/$', manufacturer_list_view, name='manufacturer_list_view'),

    ################ *** Create View *** #################
    re_path(r'^order/create/(?P<product_id>\d+)/$', order_create_view, name='order_create_view'),

    re_path(r'^order/delete/(?P<order_id>\d+)/$', order_remove_view, name='order_remove_view'),

    # ############# *** OrderCartViews *** ###############
    re_path(r'^order/clean-cart/$', cart_clean_view, name='cart_clean_view')

    # re_path(r'^manufacturers/update/$', manufacturer_update_view, name='manufacturer_detailed_view'),

]