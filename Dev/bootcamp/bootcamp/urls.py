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
# from django.views.generic import api_views
from products.views import (
    HomePageView,
    ProductListView,
    TemplateView,
    method_view,
)

from bootcamp.views import (
    handler400,
    handler403,
    handler404,
    search_view,
    search_venues,
    feedback_form_view,
    panda_link_view,
    test_request_context_view
)

from accounts.api.views import (
    GoogleSocialAuthAPIView,
    FBSocialAuthAPIView,
    GoogleSocialAuthAPIView,

)

# *** handlers 400, 403, 404, 500 *** #
handler400 = 'bootcamp.views.handler400'
handler403 = 'bootcamp.views.handler403'
handler404 = 'bootcamp.views.handler404'
handler500 = 'bootcamp.views.handler500'

# url_patterns list do not comply to PEP8 in order to save readability
urlpatterns = [
    # *** HomepageView *** #
    path('', HomePageView.as_view(), name='index'),
    path('admin/', admin.site.urls, name='admin'),

    # *** about panda hardware website *** #
    re_path('panda-hardware/', panda_link_view, name='panda_link'),

    # *** Generic ProductListView *** #
    re_path(r'^products/list3/$', ProductListView.as_view(), name='product_list_view'),

    # *** just for getting a method *** #
    re_path(r'^methods/$', method_view, name='method_view'),

    # *** search + other features views *** #
    re_path(r'^search/$', search_view, name='search_view'),
    re_path(r'^search-venues/$', search_venues, name='search_venues'),

    # *** feedback form *** #
    re_path(r'^feedback/$', feedback_form_view, name='feedback_form_view'),
    re_path(r'^access-status/$', TemplateView.as_view(template_name='access_status.html'), name='access_status'),

    # include other apps urls
    re_path(r'^', include('products.urls')),
    re_path(r'^', include('manufacturer.urls')),
    re_path(r'^', include('orders.urls')),
    re_path(r'^', include('emails.urls')),
    re_path(r'^', include('accounts.urls')),

    # *** Panda Hardware API URLS *** #
    re_path(r'^api/users/', include(('accounts.api.urls', 'api-users'), namespace='api-users')),
    re_path(r'^api/products/', include(('products.api.urls', 'api-products'), namespace='api-products')),
    re_path(r'^api/manufacturers/', include(('manufacturer.api.urls', 'api-manufacturers'), namespace='api-manufacturers')),
    re_path(r'^api/orders/', include(('orders.api.urls', 'api-orders'), namespace='api-orders')),

    # *** OAuth2 Authnetication urls *** #
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^o/sighn-in/$', GoogleSocialAuthAPIView.as_view(), name='oauth_user-login'),
    # + FacebookSocialApiView
    # + TwitterkSocialApiView

    # *** PayPal payment notification (IPN) views *** #
    path('paypal/', include('paypal.standard.ipn.urls')),

    # *** Context, RequestContext test views *** #
    re_path(r'^request-context/test/$', test_request_context_view, name='request_context-view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
