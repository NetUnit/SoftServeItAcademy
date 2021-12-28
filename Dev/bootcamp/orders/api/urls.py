from django.urls import path, re_path
from .views import OrderCrudView

urlpatterns = [
    re_path(r'^(?P<pk>\d+)$', OrderCrudView.as_view(), name='order-crud')
]