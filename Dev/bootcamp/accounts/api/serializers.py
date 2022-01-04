
from rest_framework import serializers
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.fields import (
    CharField, 
    EmailField
    )

from rest_framework.serializers import (
    CharField,
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

    def create(self, validated_data):
        '''
            Password hashing is implemented with model behavior.
            Just use the data dict as a variable
            :returns: new user object created & via POST method
        '''
        model = CustomUser()
        user = model.create_user(data=validated_data)
        if not user:
            raise ValidationError(
                {'detail': 'User hasn\'t been created ヽ(冫、)ﾉ',}
            )
        user.save()
        # print(user.__dict__)
        return user

    def validate(self, data):
        email = data.get('email')
        qs = CustomUser.objects.filter(email=email)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError(
                {'detail': 'Email already exists ┐(‘～` )┌', }
            )
        print(email)
        return data
        
class CustomUserLoginSerializer(serializers.ModelSerializer):
    username = CharField(required=False, allow_blank=True,
                        allow_null=True, max_length=42
                    )
    email = EmailField(label='Email Address', required=False, allow_blank=True)
    token = CharField(allow_blank=True, read_only=True)
    
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
        # print(data)
        email = data.get('email')
        username = data.get('username')
        if not email and not username:
            raise serializers.ValidationError(
                {'detail': 'Email/Username are required ┐(°,ʖ°)┌', }
            )
        
        data = dict(data)
        user_exists = CustomUser.user_exists(data)
            
        if not user_exists:
            raise serializers.ValidationError(
                {'detail': 'Email/Username are not valid ʅ(°_°)ʃ', }
            )

        user = CustomUser.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        
        user = user.exclude(email__isnull=True)
        user = user.first()
        print(user)
        if user:
            correct_psw = user.check_password(data.get('password'))
            raise serializers.ValidationError(
                {'detail': 'Hmm passsword wasn\'t correct (° -°）', }
            )
        data['token'] = 'Some Random Token'
        return data
