from django.urls import path, re_path
from manufacturer.api.views import ManufacturerCrudView

urlpatterns = [
    re_path(r'^(?P<pk>\d+)$', ManufacturerCrudView.as_view(), name='manufacturer-crud')
]