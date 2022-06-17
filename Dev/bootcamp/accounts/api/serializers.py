from rest_framework import serializers
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q
from .google import Google
from .facebook import Facebook
from .twitter import Twitter
from bootcamp.settings import LOGGER
import os

from bootcamp.settings import AUTH_PROVIDERS
from rest_framework_jwt.settings import api_settings
from django.http import HttpResponse
import datetime
from django.utils import timezone
from rest_framework_jwt import compat
# from compat import set_cookie_with_token
# from rest_framework_jwt.compat import set_cookie_with_token

# generate password imports
import random
import string

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
                {'detail': 'User hasn\'t been created ヽ(冫、)ﾉ'}
            )
        user.save()
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
                         allow_null=True, max_length=42)
    email = EmailField(label='Email Address', required=False,
                       allow_blank=True)
    token = CharField(allow_blank=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
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
        user = user.first()

        if not user:
            raise serializers.ValidationError(
                {'detail': 'User wasn\'tfound (° -°）', }
            )
        correct_psw = user.check_password(data.get('password'))
        print(correct_psw)
        if not correct_psw:
            raise serializers.ValidationError(
                {'detail': 'Hmm ... passsword wasn\'t correct (° -°）', }
            )
        token = Token.objects.filter(user=user).get()

        if token:
            data['token'] = token.key
        return data


class SocialAuth:
    '''
        ===========================================================
        Represents replicable logic responsible for Social Auth
        ===========================================================

        .. note::
            CustomUser - auth user model for authentication
    '''
    @staticmethod
    def register_social_user(data):
        '''
            creates a new user object with dragged email & generates passowrd
            :returns: new user object
        '''
        user = CustomUser()
        print(f"This is data: {data} is serializer")
        # generates user password
        _password = ''.join(
            [random.choice(string.digits +
                           string.ascii_letters +
                           string.punctuation) for i in range(0, 10)]
        )

        # *** !!! FOR LATER !!! *** #
        # *** build logic with sending the password to the email before
        # hashing it ***
        # sends data to users email ("e.g." password or login data)
        # :returns: dict with prepared data for registartion
        # https://realpython.com/python-send-email/
        # ---> send password here logic

        # creates user and hash the password here
        data['password'] = _password
        # user = user.create_user(data)
        return data

    # make the same with auth2_provider_model
    @staticmethod
    def check_user_exists(email=None, username=None):
        '''
        checks whether user object with such email already exists in the db
        :returns: user object id exists or None if opposite
        '''
        user = CustomUser.objects.filter(
                    Q(email=email) |
                    Q(username=username)
                ).distinct()

        users = user.exclude(email__isnull=True)
        user_exists = len(users) > 0
        user = user.first()
        return user if user_exists else None

    # *** !!! FOR LATER !!! *** #
    # build authentication here with JWT token
    # integrate with auth2_provider_model


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
            print(auth_token)
            google_user_data = Google.validate(auth_token)
            print(f'This is google user data: {google_user_data}')
            LOGGER.info(f"This is google user data: {google_user_data}")

        except Exception as err:
            print(f'Err Validation Serializer: {err}')
            raise serializers.ValidationError(
                {'detail': 'Token is either invalid or expired (︶︹︺)', }
            )

        try:
            if google_user_data['aud'] != os.environ.get(
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

        # assign user_id/provider if other thah Customuser is saved
        user_id = google_user_data.get('sub')
        provider = ''.join(
            [provider for provider in AUTH_PROVIDERS
             if len(google_user_data['iss'].split(provider)) > 1]
        )

        data = dict()
        data['email'] = google_user_data.get('email')
        data['username'] = google_user_data.get('name')
        # google image is secure content
        # data['image'] = google_user_data.get('picture')
        # get to know how to save to social_auth db
        # data['user_id'] = user_id
        # data['provider'] = provider
        # print(f"this is username: {username}") ## +++

        user = SocialAuth.check_user_exists(
            email=data['email'],
            username=data['username']
        )

        if user is None:
            return data
        return user


class FBSocialAuthSerializer(serializers.Serializer):
    '''
    Handles Serialization of Facebook Auth Data
    checks if access_token is not outdated.
    access token is an opaque string that identifies a user, app, or Page
    & can be used by the app to make graph API calls.
    When someone connects with an app using Facebook Login and approves the
    request for permissions, the app obtains an access token that provides
    temporary, secure access to Facebook APIs.
    :returns: user obj or new user object if such user isnt exist in the db
    :raises: ValidationError if Token is either fake or expired

    .. note::
        facebook-sdk lib used to achieve user data and validation
        querying the FB GraphAPI
    '''
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):

        try:
            # user data is dict
            user_data = Facebook.validate(auth_token)
            print(f"This is user data FACEBOOK:  {user_data}")
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
            return user

        except Exception:
            identifier = serializers.ValidationError(
                {'detail': 'Token is either invalid or expired (︶︹︺)', }
            )
            LOGGER.warning(f'{identifier}')
            raise identifier


class TwitterSocialAuthSerializer(serializers.Serializer):
    '''
    Handles Serialization of user object obtained
    via retrieved Twiter Auth Data.
    As access tokens provide info about user from Twitter API
    2 parameter fields has been set
    Checks also if request is being sent with 'Django Bootcamp'
    with validate_twitter_auth_tokens() and cosumer keys
    passed to last, consumer keys aren't fake
    :returns: user obj or new user data if such user isnt exists
    in the db
    :raises: ValidationError if Token is either fake or expired

    .. note::

        parsing the db with received data from twiiter API
        & checks wheteher such user already exist

        creates new user object, assighns psw automatically
        & sends it to user's email if such a user not present in
        the db
    '''
    access_token_key = serializers.CharField()
    access_token_secret = serializers.CharField()

    def validate(self, attrs):

        try:
            access_token_key = attrs.get('access_token_key')
            access_token_secret = attrs.get('access_token_secret')

            user_data = Twitter.validate_twitter_auth_tokens(
                access_token_key,
                access_token_secret
            )

            # return user_data
            email = user_data.get('email')
            username = user_data.get('screen_name')

            result = SocialAuth.check_user_exists(
                email=email,
                username=username
            )

            result.access_token_key = access_token_key
            result.access_token_secret = access_token_secret

            if result is None:
                return user_data
            return result

        except Exception as err:
            print(err)
            identifier = serializers.ValidationError(
                {'detail': 'Token is invalid or expired (︶︹︺)', }
            )
            LOGGER.warning(f'{identifier}')
            raise identifier

class TokenAuthSerializer(serializers.Serializer):

    auth_token = serializers.CharField()

    def validate(self, attrs):
        return attrs
