from rest_framework import generics, viewsets, mixins
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q

from accounts.models import CustomUser


from .serializers import (
    CustomUserLoginSerializer,
    CustomUserCreateSerializer
)


class CustomUserCreateView(generics.CreateAPIView):
    
    # model = get_user_model()
    model = CustomUser
    serializer_class = CustomUserCreateSerializer
    queryset = CustomUser.objects.all()





#     {
#     "username": "andriyproniyk@gmail.com",
#     "email": "andriyproniyk@gmail.com",
#     "password": "Aer0p0rt1715418"
# }