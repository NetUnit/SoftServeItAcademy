"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from products import views
from products.views import (
    home_view,
    HomePageView,
    product_list_view,
    ProductListView,
    product_detailed_view,
    api_product_detailed_view,
    method_view,
    product_create_view
)

from django.conf import settings
from django.conf.urls.static import static


################### *** exceptions:404, 500, 403, 400 *** #########################
# handler404 = 'products.views.handler404'
# handler500 = 'products.views.handler500'
# handler403 = 'products.views.handler403'
# handler400 = 'products.views.handler400'
###################################################################################

urlpatterns = [
    ############# *** HomepageView *** #############
    ## create html for HomePageView in templates
    path('', HomePageView.as_view(), name='index'), # add template                                  # same_3

    path('search/', home_view, name='search'),                                                      # same_3
    path('admin/', admin.site.urls, name='admin'),

    ############# *** ProductListView *** ############                                             
    re_path(r'^products/list/$', product_list_view, name='list_view'),                             # same_4
    re_path(r'^products/list2/$', ProductListView.as_view(), name='list_view'),                    # same_4  ## alternatively +++
    #################################################################################
    # path('products/<int:pk>/', views.product_detailed_view, name='detailed_view'),                # same_1
    # path('api/products/<int:pk>/', views.product_api_detailed_view, name='api_detailed_view')     # same_2

    ################### *** re_path *** #########################
    ## can adjust the number of products via quantifiers ##
    # re_path(r'^products/(?P<pk>[1-9]{1,3})/$', views.product_detailed_view, name='detailed_view'), # same_1
    # re_path(r'^api/products/(?P<pk>[1-9]{1,3})/$', views.api_product_detailed_view, name='detailed_view'), # same_2

    ## reg.ex var2 ##
    re_path(r'^products/(?P<pk>\d+)/$', product_detailed_view, name='detailed_view'), # same_1
    re_path(r'^api/products/(?P<pk>\d+)/$', api_product_detailed_view, name='detailed_view'), # same_2

    ################### *** examples *** ########################
    #path('products/1/', views.product_detailed_view, name='product-1'),

    ################### *** just for getting a method *** ########################
    re_path(r'^methods/$', method_view, name='method_view'),

    ################ *** Bad View Requests *** #################
    re_path(r'^products/create/$', product_create_view, name='product_create_view'),

    # ## ** get current app_name --> context_processors ** ##
    # re_path(r'^', include('products.urls')),
    # re_path(r'^', include('emails.urls')),
    # re_path(r'^', include('profiles.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)