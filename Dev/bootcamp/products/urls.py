from django.urls import path, re_path
from products import views
from products.views import (
    product_list_frontend_logic,
    product_list_view,
    product_create_view,
    product_detailed_view,
    api_product_detailed_view,
    product_update_view
    
)

from .models import Product
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    
    # ################### *** Detailed View *** ########################
    # # path('products/1/', views.product_detailed_view, name='product-1'),
    # # path('products/<int:pk>/', views.product_detailed_view, name='detailed_view'),                # same_1
    # # path('api/products/<int:pk>/', views.product_api_detailed_view, name='api_detailed_view')     # same_2

    # ################### * with re_path * #########################
    # ## can adjust the number of products via quantifiers ##
    # # re_path(r'^products/(?P<pk>[1-9]{1,3})/$', views.product_detailed_view, name='detailed_view'), # same_1
    # # re_path(r'^api/products/(?P<pk>[1-9]{1,3})/$', views.api_product_detailed_view, name='detailed_view'), # same_2

    # ## reg.ex var2 ##
    # re_path(r'^products/(?P<pk>\d+)/$', product_detailed_view, name='detailed_view'), # same_1
    # re_path(r'^api/products/(?P<pk>\d+)/$', api_product_detailed_view, name='detailed_view'), # same_2


    ################# *** ProductListView *** #################
    re_path(r'^products/list/$', product_list_frontend_logic, name='list_view'),                 # main#1 (fancy template)
    re_path(r'^products/list2/$', product_list_view, name='product_list_view'),                  # same_4
    
    #################################################################################
    re_path(r'^products/(?P<product_id>\d+)/$', product_detailed_view, name='detailed_view'), # same_1
    re_path(r'^api/products/(?P<product_id>\d+)/$', api_product_detailed_view, name='api_detailed_view'), # same_2

    ################## *** Create View *** #################
    re_path(r'^products/create/$', product_create_view, name='product_create_view'),

        ################## *** Update View *** #################
    re_path(r'^products/create/$', product_update_view, name='product_update_view'),

]
