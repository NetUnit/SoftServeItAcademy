# from django.conf.urls.static import static
# from django.conf.urls import include
from django.urls import path, re_path
from accounts.views import (
    login_view,
    register_view,
    # authentication,
    accounts_list_view,

)

app_name = 'accounts'

urlpatterns = [

    re_path(r'^accounts/list/$', accounts_list_view, name='accounts_list_view'),
    re_path(r'^accounts/register$', register_view, name='register'),
    re_path(r'^accounts/login$', login_view, name='login'),
    # re_path(r'^accounts/authentication', authentication, name='authentication')

    
    
]