from .views import (
    ProductCrudView,
     ProductViewSet
)

from rest_framework import routers
from django.urls import path, re_path

urlpatterns = [
    # path(r'<int:pk>', BlogPostRudView.as_view(), name='post-crud'),
    re_path(r'^(?P<pk>\d+)$', ProductCrudView.as_view(), name='product-crud'),
    re_path(r'product/(?P<pk>\d+)', ProductViewSet.as_view({'get': 'product', 'put': 'product'}), name='product-view-set')
]

# path('', include(router.urls)),
# router = DefaultRouter()
# router.register(r'product', ProductViewSet, basename='product')
# #urlpatterns = router.url