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
#from django.views.generic import api_views
from products.views import (
    home_view,
    HomePageView,
    ProductListView,
    TemplateView,
    method_view,
    search_view,
    search_venues,
)

from accounts.views import (
    panda_link_view,
    contact_view
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

    re_path('panda-hardware/', panda_link_view, name='panda_link'),
    re_path('contact/', contact_view, name='contact'),

    ############# *** HomepageView *** #############
    #!! create html for HomePageView in templates
    path('', HomePageView.as_view(), name='index'), # add template                                  # same_1

    path('home/', home_view, name='search'),                                                      # same_1
    path('admin/', admin.site.urls, name='admin'),

    ############# *** Generic ProductListView *** ############                                             
    re_path(r'^products/list3/$', ProductListView.as_view(), name='product_list_view'),             # same_3

    ################### *** just for getting a method *** ########################
    re_path(r'^methods/$', method_view, name='method_view'),
    
    ################### *** search view *** ########################
    re_path(r'^search/$', search_view, name='search_view'),             # same_3
    re_path(r'^search-venues/$', search_venues, name='search_venues'),  # same_3

    re_path(r'^', include('products.urls')),
    re_path(r'^', include('manufacturer.urls')),
    re_path(r'^', include('orders.urls')),
    re_path(r'^', include('emails.urls')),
    re_path(r'^', include('accounts.urls')),

    ################### *** payments views *** ########################
    path('paypal/', include('paypal.standard.ipn.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)