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
from django.conf.urls.static import static
from products import views
#from django.views.generic import api_views
from products.views import (
    HomePageView,
    ProductListView,
    TemplateView,
    method_view,
)

from accounts.views import (
    panda_link_view,
    contact_view,
)

from bootcamp.views import (
    handler400,
    handler403,
    handler404,
    search_view,
    search_venues,
    logger_error_view,
)


############## *** handlers 400, 403, 404, 500 *** ###################
handler400 = 'bootcamp.views.handler400'
handler403 = 'bootcamp.views.handler403'
handler404 = 'bootcamp.views.handler404'
handler500 = 'bootcamp.views.handler500'
#######################################################################



urlpatterns = [
    # 
    path('', HomePageView.as_view(), name='index'), # add template                                  # same_1
    path('admin/', admin.site.urls, name='admin'),

    # accounts
    re_path('panda-hardware/', panda_link_view, name='panda_link'),
    re_path('contact/', contact_view, name='contact'),

    ############# *** HomepageView *** #############
    #!! create html for HomePageView in templates

    ############# *** Generic ProductListView *** ############                                             
    re_path(r'^products/list3/$', ProductListView.as_view(), name='product_list_view'),             # same_3

    ################### *** just for getting a method *** ########################
    re_path(r'^methods/$', method_view, name='method_view'),
    
    ################### *** search view *** ########################
    re_path(r'^search/$', search_view, name='search_view'),             # same_3
    re_path(r'^search-venues/$', search_venues, name='search_venues'),  # same_3

    #### **** exceptions *** ####
    ## add 500, 400 & 403 exceptions here
    
    # ________________________
    re_path(r'^logger-error/$', logger_error_view, name='logger_error_view'),  # same_3

    ## 

    re_path(r'^', include('products.urls')),
    re_path(r'^', include('manufacturer.urls')),
    re_path(r'^', include('orders.urls')),
    re_path(r'^', include('emails.urls')),
    re_path(r'^', include('accounts.urls')),

    ################### *** payments views *** ########################
    path('paypal/', include('paypal.standard.ipn.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)