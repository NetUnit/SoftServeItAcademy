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

from accounts.api.views import(
    google_auth_view,
    fb_auth_view,
    twitter_auth_view,
    redir_to_fb_login,
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts_api'

urlpatterns = [
    re_path(r'^user/sighn-up/$', CustomUserCreateView.as_view(), name='user-create'),
    re_path(r'^user/sighn-in/$', CustomUserLoginView.as_view(), name='user-login'),
    
    ### JWT Authnetication urls ###
    re_path(r'^auth/token/$', obtain_jwt_token),
    re_path(r'^auth/token-verify/$', verify_jwt_token),
    re_path(r'^auth/token-refresh/$', refresh_jwt_token),

    ### Token Authnetication urls ###
    # registration view already exists
    # use postman to send POST requests
    re_path(r'^authtoken-get/$', obtain_auth_token, name='obtain-auth-token'),

    ### OAuth2 urls ###
    # re_path(r'^authtoken-get/$', obtain_auth_token, name='obtain-auth-token'),

    ### Social Auth urls ###
    re_path(r'^o/google-sighn-in-test/$', google_auth_view, name='google-user-login-test'),
    re_path(r'^o/fb-sighn-in-test/$', fb_auth_view, name='fb-user-login-test'),
    re_path(r'^o/twitter-sighn-in-test/$', twitter_auth_view, name='twitter-user-login-test'),

    ### redirect urls ###
    re_path(r'^o/fb-sighn-in-test-redir/$', redir_to_fb_login, name='fb-user-login-test-redir'),
    
]
