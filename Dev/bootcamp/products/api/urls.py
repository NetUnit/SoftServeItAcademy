from .views import ProductCrudView
from django.urls import path, re_path

urlpatterns = [
    # path(r'<int:pk>', BlogPostRudView.as_view(), name='post-crud'),
    re_path(r'^(?P<pk>\d+)$', ProductCrudView.as_view(), name='product-crud'),
]