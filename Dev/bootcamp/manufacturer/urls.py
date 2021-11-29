from django.conf.urls import include
from django.urls import path, re_path
from manufacturer.views import (

    manufacturer_create_view,
    manufacturer_list_view,
    manufacturer_detailed_view,
    api_manufacturer_detailed_view,
    manufacturer_update_view,
    manufacturer_delete_view,
    media_download_view,
    get_products_manufacturer
)

from django.conf import settings

app_name = 'manufacturer'

urlpatterns = [
    
    ############# *** ManufacturerDeatailedView + API *** ###############
    re_path(r'^manufacturers/(?P<manufacturer_id>\d+)/$', manufacturer_detailed_view, name='detailed_view'),
    re_path(r'^api/manufacturers/(?P<manufacturer_id>\d+)/$', api_manufacturer_detailed_view, name='api_detailed_view'),

    ############# *** ManufacturerListView *** ###############
    re_path(r'^manufacturers/list/$', manufacturer_list_view, name='manufacturer_list_view'),

    ################ *** Create View *** #################
    re_path(r'^manufacturers/create/$', manufacturer_create_view, name='manufacturer_create_view'),

    ############# *** ManufacturerUpdateView *** ###############
    re_path(r'^manufacturers/update/(?P<manufacturer_id>\d+)/$', manufacturer_update_view, name='manufacturer_update_view'),

    ############# *** ManufacturerDeleteView *** ###############
    re_path(r'^manufacturers/delete/(?P<manufacturer_id>\d+)/$', manufacturer_delete_view, name='manufacturer_delete_view'),

    ################## *** media download product *** ###############
    re_path(r'^manufacturers/media-download/(?P<manufacturer_id>\d+)/$', media_download_view, name='media_download_view'),

    ################## *** get products manufacturer *** ###############
    re_path(r'^manufacturers/get-products-manufacturer/(?P<manufacturer_id>\d+)/$', get_products_manufacturer, name='get_products_manufacturer')

]