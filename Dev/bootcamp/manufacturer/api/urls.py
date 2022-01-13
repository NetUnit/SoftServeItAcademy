from django.urls import path, re_path
from manufacturer.api.views import (
    ManufacturerCrudView,
    ManufacturerCreateAPIView,
    ManufacturerMixinAPIView
)

urlpatterns = [
    re_path(r'^(?P<pk>\d+)$', ManufacturerCrudView.as_view(), name='manufacturer-crud'),
    re_path(r'^manufacturer/create/$', ManufacturerCreateAPIView.as_view(), name='manufacturer-create'),
    re_path(r'^list/$', ManufacturerMixinAPIView.as_view(), name='manufacturer-list-create'),
]