from django.conf.urls import include
from django.urls import path, re_path
from manufacturer.views import (

    manufacturer_create_view,
    manufacturer_list_view,
    manufacturer_detailed_view,
    api_manufacturer_detailed_view,
    manufacturer_update_view
)

from django.conf import settings

app_name = 'manufacturer'

urlpatterns = [

    ################ *** Create View *** #################
    re_path(r'^manufacturers/create/$', manufacturer_create_view, name='manufacturer_create_view'),

    ############# *** ManufacturerListView *** ###############
    re_path(r'^manufacturers/list/$', manufacturer_list_view, name='manufacurer_list_view'),

    ############# *** ManufacturerDeatailedView + API *** ###############
    re_path(r'^manufacturers/(?P<manufacturer_id>\d+)/$', manufacturer_detailed_view, name='manufacturer_detailed_view'),
    re_path(r'^api/manufacturers/(?P<manufacturer_id>\d+)/$', api_manufacturer_detailed_view, name='api_manufacurer_list_view'),

    ############# *** ManufacturerUpdateView *** ###############
    re_path(r'^manufacturers/update/$', manufacturer_update_view, name='manufacturer_detailed_view'),

]