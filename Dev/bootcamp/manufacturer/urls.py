from django.conf.urls import include
from django.urls import path, re_path
from manufacturer.views import (

    manufacturer_create_view,
    #manufacturer_list_view
)

from django.conf import settings

app_name = 'manufacturer'

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


    # ############# *** ManufacturerListView *** ############                                             
    # re_path(r'^manufacturers/list/$', manufacturer_list_view, name='manufacturer_list_view'),        # same_4
    # re_path(r'^products/list2/$', ProductListView.as_view(), name='list_view'),                    # same_4  ## alternatively +++
    # re_path(r'^products/list3/$', product_list_frontend_logic, name='list_view2'),                 # same_4 (fancy template)
    # #################################################################################


    # ################ *** Create View *** #################
    #re_path(r'^manufacturers/create/$', manufacturer_create_view, name='manufacturer_create_view'),

]