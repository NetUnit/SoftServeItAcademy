from django.urls import path, re_path
from products import views
from products.views import (
    product_list_view,
    product_list_view2,
    product_create_view,
    product_detailed_view,
    api_product_detailed_view,
    product_update_view,
    product_delete_view,
    media_download_view,
)

from .models import Product
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    # *** Product Deatailed View + API *** #
    re_path(r'^products/(?P<product_id>\d+)/$', product_detailed_view, name='detailed_view'),
    re_path(r'^api/products/(?P<product_id>\d+)/$', api_product_detailed_view, name='api_detailed_view'),

    # *** Product List View *** #
    re_path(r'^products/list/$', product_list_view, name='product_list_view'),
    # generic django view for lists
    re_path(r'^products/list2/$', product_list_view2, name='product_list_view2'),

    # *** Product Create View *** #
    re_path(r'^products/create/$', product_create_view, name='product_create_view'),

    # *** Product Update View *** #
    re_path(r'^products/update/(?P<product_id>\d+)/$', product_update_view, name='product_update_view'),

    # *** Delete View *** #
    re_path(r'^products/delete/(?P<product_id>\d+)/$', product_delete_view, name='product_delete_view'),

    # *** media download product *** #
    re_path(r'^products/download-media/(?P<product_id>\d+)/$', media_download_view, name='media_download_view'),
]
