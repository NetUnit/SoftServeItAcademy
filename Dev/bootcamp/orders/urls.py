from django.conf.urls import include
from django.urls import path, re_path
from orders.views import (
    order_detailed_view,
    order_create_view,
    cart_view
)

from django.conf import settings

app_name = 'orders'

urlpatterns = [
    
    re_path(r'order/cart/', cart_view, name='cart_view'),

    # ############# *** ManufacturerDeatailedView + API *** ###############
    re_path(r'^order/(?P<order_id>\d+)/$', order_detailed_view, name='detailed_view'),
    # re_path(r'^api/manufacturers/(?P<manufacturer_id>\d+)/$', api_manufacturer_detailed_view, name='api_detailed_view'),

    # ############# *** ManufacturerListView *** ###############
    # re_path(r'^manufacturers/list/$', manufacturer_list_view, name='manufacturer_list_view'),

    ################ *** Create View *** #################
    re_path(r'^order/create/$', order_create_view, name='manufacturer_create_view'),

    # ############# *** ManufacturerUpdateView *** ###############
    # re_path(r'^manufacturers/update/$', manufacturer_update_view, name='manufacturer_detailed_view'),

]