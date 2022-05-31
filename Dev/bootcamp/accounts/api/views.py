from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics, viewsets, mixins, permissions
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from accounts.models import CustomUser
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate, login
from rest_framework import serializers
from django.core import serializers as dj_serializer

from bootcamp.settings import (
    LOGGER,
)

import logging
import sys
import os
from django.views.generic import TemplateView
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from rest_framework.response import Response
import facebook
import traceback
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3 import connectionpool
from requests.adapters import HTTPAdapter
import collections
import io
from asyncio import StreamReader
import asyncio
import urllib.parse
import gnupg
import subprocess
from requests.packages import urllib3

from .serializers import (
    CustomUserCreateSerializer,
    CustomUserLoginSerializer,
    GoogleSocialAuthSerializer,
    FBSocialAuthSerializer,
    TwitterAuthSerializer,
    SocialAuth
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)

from django.contrib.auth import authenticate, login
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect
)

from django.http import (
    HttpResponse,
    JsonResponse,
    Http404,
    HttpResponseRedirect
)


class CustomUserCreateView(generics.CreateAPIView):

    model = get_user_model()
    serializer_class = CustomUserCreateSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]


class CustomUserLoginView(APIView):

    permission_classes = [permissions.AllowAny]
    model = get_user_model()
    serializer_class = CustomUserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        # print(request.user)
        # print(request.auth)
        serializer = CustomUserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            return Response(data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def perform_authentication(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        _password = request.data.get('password')
        email = username if not email else email
        user = authenticate(request, username=email, password=_password)
        login(request, user) if user else serializers.ValidationError(
            {'detail': 'Seem\'s like that username or email was wrong (⇀‸↼‶)'},
        )


class GoogleSocialAuthAPIView(GenericAPIView):

    template = 'accounts/snippets/google_login.html'
    serializer_class = GoogleSocialAuthSerializer
    # renderer_classes = [TemplateHTMLRenderer, template]

    def post(self, request, *args, **kwargs):
        '''
            posted data from google with auth_token & auth_token_id

        '''

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # data = serializer.validated_data
        data = dict(serializer.validated_data)
        user = data.get('auth_token')
        # django serializer to_str
        # user_data = dj_serializer.serialize('json', [user, ])
        # data = serializer.validated_data.get('auth_token')
        return Response(serializer.data, status=HTTP_200_OK)


class FBSocialAuthAPIView(GenericAPIView):

    serializer_class = FBSocialAuthSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # data = serializer.validated_data
        data = dict(serializer.validated_data)
        print(f"This is serializer data FB: {data}")
        # user = data.get('auth_token')
        # django serializer to_str
        # user_data = dj_serializer.serialize('json', [user, ])
        # data = serializer.validated_data.get('auth_token')
        return Response(serializer.data, status=HTTP_200_OK)


class TwitterSocialAuthAPIView(GenericAPIView):
    
    serializer_class = TwitterAuthSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # data = serializer.validated_data
        data = dict(serializer.validated_data)
        print(f"This is serializer data Twitter: {data}")
        user = data.get('auth_token')
        # django serializer to_str
        # user_data = dj_serializer.serialize('json', [user, ])
        # data = serializer.validated_data.get('auth_token')
        return Response(serializer.data, status=HTTP_200_OK)

def google_auth_view(request, *args, **kwargs):
    '''
        is a Google IdToken for user authnentication

        :returns: Google IdToken
        :rtype: str

        .. note:: 
            subsequent parameters: 
                * body: data sent by the client to our API
                * value: bytes from the body response
                * decoded_string: str data from bytes 
                * data: dict(), another way of getting IdToken 
    '''
    serializer_class = GoogleSocialAuthSerializer
    user = CustomUser()
    # print(request.META.get('PATH_INFO'))
    # print(f'{request.POST} This is post')
    # print(request.META.get('GOOGLE_CLIENT_ID'))
    # print(request.META.get('GOOGLE_CLIENT_SECRET'))
    # print(request.META.get('data'))

    # POST method is acquired via JS in a template

    if request.method == 'POST':
        # print(request.user.is_authenticated)
        serializer = serializer_class()

        try:
            # 2 METHODS using JS POST fetch url
            # get bytes API request
            # value = request.body
            # # from bytes to str dict data
            # decoded_string = value.decode()
            # token = eval(decoded_string).get('IdToken')

            # another way of getting IdToken
            # data = json.loads(request.body)
            # print(data)
            # token = data['IdToken']

            # raw request method data
            raw_data = request.body
            # print(f'{raw_data} this are bytes')
            decoded_string = raw_data.decode()
            # print(f'{decoded_string} this are decoded string1')
            decoded_string = eval(decoded_string)
            # print(f'{decoded_string} this are decoded string2')
            token = decoded_string.get('IdToken')
            print(token)

            # result is user data from google db
            result = serializer.validate_auth_token(token)

            print(f'This is result: {result}')

            # register user here
            if isinstance(result, dict):
                user_data = result
                print(f"This is user_data | view: {user_data}")

                user_data = SocialAuth.register_social_user(
                    user_data
                )

                print(f'This is user_data in a view: {user_data}')

                email = user_data.get('email')
                _password = user_data.get('password')

                # authenticate & create_user dropped here
                # in order to test authenticate method
                user = user.create_user(user_data)
                user = authenticate(
                    request, username=email, password=_password)

                login(request, user, backend='accounts.backends.EmailBackend')

                messages.success(
                    request,
                    f'U\'ve just created the next user: {user} (^_-)≡☆'
                )

                # return render (request, 'accounts/sm_register_success.html', context={'user': user})
                return render(request, 'accounts/snippets/google_login.html', context={'user': user})

            # login user
            if isinstance(result, CustomUser):
                user = result
                # user authenticate here
                login(request, user, backend='accounts.backends.EmailBackend')
                # print(user.is_authenticated) ## ++
                # print(os.environ) ## ++

                messages.success(
                    request,
                    f'U\'ve just successfully logined (^_-)≡☆;;;'
                )

                return render(request, 'accounts/snippets/google_login.html', context={'user': user})

        except Exception as err:
            print(err)

    return render(request, 'accounts/snippets/google_login.html', context={})


class RequestUserFilter(logging.Filter):

    def filter(self, record=None):
        record.user = record.request.user
        return record.user


# def redir_to_fb_login(request, *args, **kwargs):
#     return redirect('/api/users/o/fb-sighn-in-test/')


def fb_auth_view(request, *args, **kwargs):
    '''
    To connect our app with Facebook or any other social media we just
    don't care about tokens. So that auth FB logic differs from google
    Middleware does workflow with tokens:
    http://django-social-auth.readthedocs.org/en/latest/configuration.html
    & http://django-social-auth.readthedocs.org/en/latest/backends/facebook.html

        .. note:: 
            can be used to parse a valid JSON string &
            convert it into a Python Dictionary

            csrf token is inside html
    '''
    user = request.user
    raw_data = request.body
    decoded_string = raw_data.decode()
    condition = len(decoded_string) > 0
    if not condition:
        return render(request, 'accounts/snippets/fb_login.html', context={'user': user})
    json_data = json.loads(raw_data)

    # print(json_data) # ++++
    user_data = json_data.get('response')
    email = user_data.get('email')
    username = user_data.get('name')

    #######################################################################
    # just to test fb_authkoken
    # auth_token = user_data.get('token')
    ########################################################################
    # in case we need to grab picture
    picture_obj = user_data.get('picture')
    picture_data = picture_obj.get('data')
    picture_url = picture_data.get('url')

    result = SocialAuth.check_user_exists(
        email=email,
        username=username
    )

    print(f"This is result: {result}")

    ################### *** new user *** #############################
    if result == None:

        # print(new_user_data) ## +++
        # creates new user object & assighn password automatically
        data = dict()
        data['username'] = username
        data['email'] = email
        data['image'] = picture_url

        new_user = Social_Auth.register_social_user(data)
        print(new_user)

    ################################################

        messages.success(
            request,
            f'U\'ve just created the next user: {new_user.username} (^_-)≡☆'
        )
        return redirect('/accounts/register-fbv/')
    ################################################
    if isinstance(result, CustomUser):

        user = result
        login(request, user, backend='accounts.backends.EmailBackend')

        print(f"AUTHENTICATED: {user.is_authenticated}")
        print(user)

        messages.success(
            request,
            f'U\'ve just successfully logined (^_-)≡☆;;;'
        )

        # return redirect('/accounts/login-success/')
        print(f'CustomUser: {user}')
        return render(request, 'accounts/snippets/fb_login.html', context={'user': user})

    return render(request, 'accounts/snippets/fb_login.html', context={'user': user})

@csrf_protect
def twitter_auth_view(request, *args, **kwargs):
    user = request.user
    serializer_class = TwitterSocialAuthSerializer

    access_token_key = os.environ.get('ACCESS_TOKEN_KEY')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

    
    print(access_token_key, access_token_secret)

    serializer = serializer_class()

    result = serializer.validate_auth_token(
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
    )

    print(f"This is result of validation VIEW: {result}")

    # user_id = user_data.get('id_str')
    # provider = user_data.get('twitter')

    email = result.get('email')
    username = result.get('screen_name')

    print(username)

    result = SocialAuth.check_user_exists(
        email=email,
        username=username
    )

    # print(result)
    # print(request.body)

    if result == None:
        # print(new_user_data) ## +++
        # creates new user object & assighn password automatically
        data = dict()
        data['username'] = username
        data['email'] = email
        data['image'] = result.get['profile_image_url']

        new_user = Social_Auth.register_social_user(data)
        print(new_user)

        messages.success(
            request,
            f'U\'ve just created the next user: {new_user.username} (^_-)≡☆'
        )

        return redirect('/accounts/register-fbv/')

    ################################################
    if isinstance(result, CustomUser):

        user = result
        login(request, user, backend='accounts.backends.EmailBackend')

        print(f"AUTHENTICATED: {user.is_authenticated}")
        print(user)

        messages.success(
            request,
            f'U\'ve just successfully logined (^_-)≡☆;;;'
        )

        
        print(f'CustomUser: {user}')
        # return redirect('/accounts/login-success/')
        return render(request, 'accounts/snippets/twitter_login.html', context={'user': user})
    ################################################

    return render(request, 'accounts/snippets/twitter_login2.html', context={'user': user})


class GoogleSocialAuthTemplateView(TemplateView, APIView):

    serializer_class = GoogleSocialAuthSerializer
    template_name = 'accounts/snippets/google_login.html'

    def get(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        return print(request.body)
        return print(request.__dict__)
