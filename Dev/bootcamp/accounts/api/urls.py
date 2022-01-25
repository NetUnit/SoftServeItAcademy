from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, re_path

from .views import (
    CustomUserCreateView,
    CustomUserLoginView,
    
)

urlpatterns = [
    re_path(r'^user/sighn-up/$', CustomUserCreateView.as_view(), name='user-create'),
    re_path(r'^user/sighn-in/$', CustomUserLoginView.as_view(), name='user-login'),
    path('auth/token/', obtain_jwt_token)
]
