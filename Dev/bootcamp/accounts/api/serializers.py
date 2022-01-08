
from rest_framework import serializers
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q
from .google import Google
import os

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

from accounts.models import (
    CustomUser,
    Token
    )

from django.contrib.auth import authenticate, login

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
        print(data)
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
        '''
            we can also assighn other than rest_framework.authtoken
            here.
            :returns: validated data that comes from a client when auth process
            :raise Vlidation Error: no user obj in the db or wrong auth data
        '''
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
        #print(user)
        user = user.first()
        #print(user)
        #print(data.get('password'))
        if not user:
            raise serializers.ValidationError(
                {'detail': 'User wasn\'tfound (° -°）', }
            )
        correct_psw = user.check_password(data.get('password'))
        if not correct_psw:
            raise serializers.ValidationError(
                {'detail': 'Hmm ... passsword wasn\'t correct (° -°）', }
            )
        token = Token.objects.filter(user=user).get()
        if token:
            data['token'] = token.key
        return data


from bootcamp.settings import AUTH_PROVIDERS


class GoogleSocialAuthSerializer(serializers.Serializer):
    
    auth_token = serializers.CharField() 

    # register new_user here
    # def register_social_user(self, email, *args, **kwargs):
    #     user = CustomUser.get_user_by_email(email)
    #     return user
    
    # authenticate user_here
    # def register_social_user(self, email, *args, **kwargs):
    #     user = CustomUser.get_user_by_email(email)
    #     user = authenticate(username=email, password='Aer0p0rt1715418')
    #     # login(user)
    #     return user

    def validate_auth_token(self, auth_token):

        try:
            user_data = Google.validate(auth_token)
            user_data['sub']
            #print(f"This is user data: {user_data}")
        except Exception as err:
            # print(f'Err: {err}')
            raise serializers.ValidationError(
                {'detail': 'Token is invalid or expired (︶︹︺)', }
            )

        ## user data is str -- thats why code below doesn't work

        try:
            # user_data['aud'] = 1089815522327-308m9crjd7u9g4t5j7qsrhttef305l1a.apps.googleusercontent.com
            # print(user_data['aud'] == os.environ.get('GOOGLE_CLIENT_ID')) ## True
            if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
                raise serializers.ValidationError(
                    {'detail': 'Oops who are U ...', }
                )
        except Exception as err2:
            print(f'Err2: {err2}')

        
        user_id = user_data.get('sub')
        #print(user_id)
        email = user_data.get('email')
        #print(email)
        name = user_data.get('name')
        #print(name)

        provider = ''.join(
            [provider for provider in AUTH_PROVIDERS
            if len(user_data['iss'].split(provider)) > 1]
        )

        # print(provider)
        # user = self.register_social_user(email)
        # print(f'This is {user}')

        return register_social_user(
            provider=provider,
            user_id=user_id,
            email=email,
            name=name
        )

        # return register_social_user(
        #     email=email,
        #     password=password
        # )