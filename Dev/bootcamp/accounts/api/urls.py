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

from accounts.api.views import (
    # API views
    GoogleSocialAuthAPIView,
    FBSocialAuthAPIView,
    TwitterSocialAuthAPIView,
    # social auth views
    google_auth_view,
    fb_auth_view,
    twitter_auth_view,
    TokenAuthView

)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts_api'

urlpatterns = [
    re_path(r'^user/sighn-up/$', CustomUserCreateView.as_view(), name='user-create'),
    re_path(r'^user/sighn-in/$', CustomUserLoginView.as_view(), name='user-login'),

    # *** JWT Authnetication urls *** #
    re_path(r'^auth/token-jwt-obtain/$', obtain_jwt_token),
    re_path(r'^auth/token-verify-jwt/$', verify_jwt_token),
    re_path(r'^auth/token-refresh-jwt/$', refresh_jwt_token),

    # *** Token Authnetication urls *** #
    # registration view already exists
    # use postman to send POST requests
    re_path(r'^authtoken-get/$', obtain_auth_token, name='obtain-auth-token'),
    re_path(r'authtoken/sighn-in/', TokenAuthView.as_view(), name='token-auth-view'),

    # *** OAuth2 urls *** #
    # re_path(r'^authtoken-get/$', obtain_auth_token, name='obtain-auth-token'),
    re_path(r'^o/google-sighn-in-test/$', GoogleSocialAuthAPIView.as_view(), name='google-user-endpoint-test'),
    re_path(r'^o/fb-sighn-in-test/$', FBSocialAuthAPIView.as_view(), name='fb-user-endpoint-test'),
    re_path(r'^o/twitter-sighn-in-test/$', TwitterSocialAuthAPIView.as_view(), name='twitter-user-endpoint-test'),

    # *** Social Auth urls *** #
    re_path(r'^o/google-sighn-in/$', google_auth_view, name='google-user-login'),
    re_path(r'^o/fb-sighn-in/$', fb_auth_view, name='fb-user-login'),
    re_path(r'^o/twitter-sighn-in/$', twitter_auth_view, name='twitter-user-login'),
]
