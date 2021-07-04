from django.conf.urls import include
from django.urls import path, re_path
from manufacturers.views import (

    manufacturer_create_view,
    manufacturer_list_view
)

from django.conf import settings

app_name = 'manufacturers'

urlpatterns = [

    ################ *** Create View *** #################
    re_path(r'^manufacturers/create/$', manufacturer_create_view, name='manufacturer_create_view'),

    ############# *** ManufacturerListView *** ###############
    re_path(r'^manufacturers/list/$', manufacturer_list_view, name='manufacurer_list_view'),

    ############# *** ManufacturerDeatailedView *** ###############


]