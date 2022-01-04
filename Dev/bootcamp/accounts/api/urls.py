from django.urls import path, re_path

from .views import (
    CustomUserCreateView,
)

urlpatterns = [
    re_path(r'^user/sighn-up/$', CustomUserCreateView.as_view(), name='user-create'),
]
