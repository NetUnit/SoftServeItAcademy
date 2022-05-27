
from rest_framework import serializers
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q
from .google import Google
from .facebook import Facebook
from bootcamp.settings import LOGGER
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
import json
from .register import register_social_user

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
from rest_framework_jwt.settings import api_settings
from django.http import HttpResponse
import datetime
from django.utils import timezone

# from rest_framework_jwt.compat import set_cookie_with_token
from rest_framework_jwt import compat
# from compat import set_cookie_with_token

class SocialAuth:

    '''
    ===========================================================
    Represents replicable logic responsible for Social Auth
    ===========================================================

    .. note:: 
        CustomUser - auth user model for authentication
    '''
    
    @staticmethod
    def send_password():
        '''
        sends data to users email ("e.g." password or login data)
        :returns: ...
        https://realpython.com/python-send-email/
        '''
        pass


    @staticmethod
    def register_social_user(data):
        print(data)
        '''
        creates a new user object with dragged email & generates passowrd
        :returns: new user object
        '''
        user = CustomUser()
        _password = ''.join(
            [random.choice(string.digits + 
            string.ascii_letters + 
            string.punctuation) for i in range(0, 10)]
            )

        ##############################################################
        # *** build logic with sending the password to the email *** #
        # print(password)
        ##############################################################

        data['password'] = _password
        # print(data)
        print(_password)

        # user = user.create_user(**data)
        # return user
        return data

    # make the same with auth2_provider_model 
    @staticmethod
    def check_user_exists(email=None, username=None):
        '''
        checks whether user object with such email already exists in the db
        :returns: user object id exists or None if opposite
        '''
        print(email)
        print(username)

        user = CustomUser.objects.filter(
                    Q(email=email) |
                    Q(username=username)
                ).distinct()

        users = user.exclude(email__isnull=True)
        user_exists = len(users) > 0
        user = user.first()
        return user if user_exists else None

    # build authentication here with JWT token  
    # integrate with with auth2_provider_model

class GoogleSocialAuthSerializer(serializers.Serializer):

    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        '''
        validates acquired with google lib token
        checks if token is not outdated.
        checks if request is being sent with 'Django Bootcamp'
        & GOOGLE_CLIENT_ID isn't fake
        :returns: user obj or new user object if such user isnt exist in the db

        .. note:: 
            google-auth lib used to achieve Token, GoogleUser and validation
            querying the Google oauth2 api
        '''
        try:
            user_data = Google.validate(auth_token)
            user_data['sub']
            print(f"This is user data: {user_data}")
        except Exception as err:
            # print(f'Err: {err}')
            raise serializers.ValidationError(
                {'detail': 'Token is invalid or expired (︶︹︺)', }
            )

        ## user data is str -- thats why code below doesn't work

        try:
            # user_data['aud'] = 1089815522327-308m9crjd7u9g4t5j7qsrhttef305l1a.apps.googleusercontent.com
            # print(user_data['aud'] == os.environ.get('GOOGLE_CLIENT_ID')) ## True
            if user_data['aud'] != os.environ.get(
                'GOOGLE_CLIENT_ID'
            ):
                raise serializers.ValidationError(
                    {'detail': 'Oops who are U ...', }
                )
        except Exception:
            identifier = serializers.ValidationError(
                {'detail': 'Token is invalid or expired (︶︹︺)', }
            )
            LOGGER.warning(f'{identifier}')
            raise identifier

        user_id = user_data.get('sub')
        email = user_data.get('email')
        name = user_data.get('name')

        provider = ''.join(
            [provider for provider in AUTH_PROVIDERS
            if len(user_data['iss'].split(provider)) > 1]
        )

        # include provider for different than CustomUser auth model
        # print(provider)

        user = SocialAuth.check_user_exists(
            email=email,
            username=username
        )

        if user is None:

            user = SocialAuth.register_social_user(
                user_id=user_id,
                email=email,
                username=name,
                # provider=provider
            )

        return user

    def get_now(self) -> datetime:
        return timezone.now()

    # assighn date 
    def user_record_login(self, user: CustomUser) -> CustomUser:
        user.last_login = self.get_now()
        user.save()
        return user

    # to dict user
    def get_user(self, user: CustomUser):

        return {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }


    def jwt_login(self, response: HttpResponse, user: CustomUser) -> HttpResponse:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER ## ++
        

        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER ## ++
        

        payload = jwt_payload_handler(user) ## ++
        # print(payload)
        # payload = json.loads(str(payload))

        # token = jwt_encode_handler(payload) ## ++
        # print(token)

        # if api_settings.JWT_AUTH_COOKIE:
        #     set_cookie_with_token(response, api_settings.JWT_AUTH_COOKIE, token)

        self.user_record_login(user=user) 

        return response

    def some_function(self,  user: CustomUser) -> CustomUser:
        self.user_record_login(user=user)
        response = Response(data=serializer.get_user(user=user)) 
        response = serializer.jwt_login(response=response, user=user)


class FBSocialAuthSerializer(serializers.Serializer):
    '''
        Handles Serialization of Facebook Auth Data
        checks if token is not outdated.
        checks if request is being sent with 'Django Bootcamp'
        & GOOGLE_CLIENT_ID isn't fake
        :returns: user obj or new user object if such user isnt exist in the db
        :raises: ValidationError if Token is either fake or expired

        .. note:: 
            facebook-sdk lib used to achieve user data and validation
            querying the FB GraphAPI
    '''
    def validate_auth_token(self, auth_token):

        try:
            # user data is dict
            user_data = Facebook.validate(auth_token)
            print(f"This is user data:  {user_data}")
            email = user_data.get('email')
            username = user_data.get('name')
            provider = 'facebook'

            user = SocialAuth.check_user_exists(email=email, username=username)

            # None if user doesn't exists in db
            if user is None:

                # user_id = user_data['id']

                user = SocialAuth.register_social_user(
                    # user_id=user_id,
                    email=email,
                    username=username,
                    # provider=provider
                )

            ### print(f'This is user: {user}') ## +++
            return user

        except Exception:
            identifier = serializers.ValidationError(
                {'detail': 'Token is invalid or expired (︶︹︺)', }
            )
            LOGGER.warning(f'{identifier}')
            raise identifier
