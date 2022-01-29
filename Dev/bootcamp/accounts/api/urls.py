from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token
)

from django.urls import path, re_path
from django.conf.urls import include

from .views import (
    CustomUserCreateView,
    CustomUserLoginView,
    
)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path(r'^user/sighn-up/$', CustomUserCreateView.as_view(), name='user-create'),
    re_path(r'^user/sighn-in/$', CustomUserLoginView.as_view(), name='user-login'),
    
    ### JWT Authnetication urls ###
    re_path(r'^auth/token/$', obtain_jwt_token),
    re_path(r'^auth/token-verify/$', verify_jwt_token),
    re_path(r'^auth/token-refresh/$', refresh_jwt_token),

    #### Token Authnetication urls ####
    # registration view already exists
    re_path(r'^authtoken-get/$', obtain_auth_token, name='obtain-auth-token'),

]