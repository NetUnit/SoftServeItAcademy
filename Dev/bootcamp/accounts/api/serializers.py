
from rest_framework import serializers
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField, 
    ValidationError
    )
from rest_framework.relations import HyperlinkedIdentityField

from accounts.models import CustomUser


class CustomUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password',   
        ]

    # def create(self, validated_data):
    #     print(validated_data)


class CustomUserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password',
            'token'   
        ]

        extra_kwargs = {'password':
                {'write_only': True}
            }
    
    def validate(self, data):


        return data