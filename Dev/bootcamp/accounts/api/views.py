from rest_framework import generics, viewsets, mixins, permissions
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q

from accounts.models import CustomUser
from django.contrib.auth import authenticate, login
from rest_framework import serializers

from bootcamp.settings import LOGGER
import logging
import sys

from .serializers import (
    CustomUserCreateSerializer,
    CustomUserLoginSerializer,
    GoogleSocialAuthSerializer,
    FBSocialAuthSerializer
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

import os

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
        #print(request.user)
        #print(request.auth)
        serializer = CustomUserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            return Response(data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def perform_authentication(self, request):
        email = request.data.get('email')
        username  = request.data.get('username')
        _password = request.data.get('password')
        email = username if not email else email
        user = authenticate(request, username=email, password=_password)
        login(request, user) if user else serializers.ValidationError(
            {'detail': 'Seem\'s like that username or email was wrong (⇀‸↼‶)'},
        )


from rest_framework.renderers import TemplateHTMLRenderer
class GoogleSocialAuthView(GenericAPIView):

    template = 'accounts/snippets/google_login.html'
    serializer_class = GoogleSocialAuthSerializer
    # renderer_classes = [TemplateHTMLRenderer, template]


    def post(self, request, *args, **kwargs):
        '''
            posted data from google with auth_token & auth_token_id

        '''
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data.get('auth_token')
        return Response(serializer.data, status=HTTP_200_OK)
    

from django.views.generic import TemplateView
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from rest_framework.response import Response

# class CustomLoginView(auth_views.LoginView):
#     form_class = LoginForm
#     template_name = 'accounts/login_form_as_p.html'

# @csrf_exempt
@csrf_protect
def google_authentication_view(request, *args, **kwargs):
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

    # print(request.META.get('PATH_INFO'))
    # print(f'{request.POST} This is post')
    # print(request.META.get('GOOGLE_CLIENT_ID'))
    # print(request.META.get('GOOGLE_CLIENT_SECRET'))
    # print(request.META.get('data'))
    
    # POST method is acquired via JS in a template

    if request.method == 'POST':
        print('This is POST method')
        # print(request.user.is_authenticated)
        serializer = serializer_class()
        # decoded_string = x.decode()
        # print(decoded_string)
        
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
            raw_data = request.__dict__.get('_body')
            # print(f'{raw_data} this are bytes')
            decoded_string = raw_data.decode()
            # print(f'{decoded_string} this are decoded string1')
            decoded_string = eval(decoded_string)
            # print(f'{decoded_string} this are decoded string2')
            token = decoded_string.get('IdToken')
            # print(token)

            # print(request.user.is_authenticated)
            ## print(token) ## ++

            result = serializer.validate_auth_token(token)
            # print(request.user.is_authenticated)
            # print(result) ## ++
            # print(isinstance(result, CustomUser)) ## ++

            # register user
            if isinstance(result, dict):

                new_user_data = result
                # print(new_user_data) ## +++
                messages.success(
                request,
                f'U\'ve just created the next user: {new_user.username} (^_-)≡☆'
                )
                return redirect ('/accounts/register-fbv/')

            # login user
            if isinstance(result, CustomUser):
                    # print(request.method) ## POST
                    # print(result)

                # if not request.user == result:
                #     print(result)
                #     return redirect('accounts/check-user-auth/')
                #     # return redirect('/accounts/login-failed/')
                #     return render (request, 'user_status.html', context={'result': result})

                user = result
                login(request, user, backend='accounts.backends.EmailBackend')
                print(user.is_authenticated)
                print(os.environ) 

                ### google client id will be here: 'GOOGLE_CLIENT_ID': '1089815522327-308m9crjd7u9g4t5j7qsrhttef305l1a.apps.googleusercontent.com'
                # WSGI POST
                ## <Response status_code=200, "text/html; charset=utf-8">

                ### ***** ###
                # res = serializer.authenticate_social_user(request=request, user=user)
                # print(res)
                messages.success(
                    request,
                    f'U\'ve just successfully logined (^_-)≡☆;;;'
                )
                # print('dsd')
                # print(user)
                # return redirect('/accounts/login-success/')
                print(f'CustomUser: {user}')
                # return redirect('/accounts/login-success/')
                return render (request, 'accounts/snippets/google_login.html', context={'user': user})
                # return redirect ('/panda-hardware/')

        except Exception as err:
            print(err)

    # user = request.user
    # print(f'GET: {user}')
    return render (request, 'accounts/snippets/google_login.html', context={})

import facebook
import traceback
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import collections

@csrf_protect
def fb_authentication_view(request, *args, **kwargs):

    # print(True, True, True)
    auth_token = "EAAOltYYj3GsBAIznd5J8DZByW9NgPq07g6Fe9XOgubk7uXkRPz6ZCs5ukZAcJ0VNMGRbCy8bxbZCnDeZCNX88QeZB4NZB1389vkiibEZAywkzvdwuuQvK4UC6aBdrNEvZCM4RTqC4TYxu83tqkHiPZCknJCnS5H5yPi3c6sURYWKLpqT8ZAPlJqGqy2RTjFQVcCuNToolm7ET2jDx2warpsftwKMZAHJqqbR1Lm3KYMZAfvP1TgZDZD"
    


    # graph = facebook.GraphAPI(access_token="EAAOltYYj3GsBAL1OILvbN5OpCx7augQjYDqZAxUeLGcggZCam56X7uUkz8aqsvG7ApSqlxzqQZCC1tmOw8wG3X1Vnrf9mhZAQ3JTbcTZB5HZCVBkf4FRzNtouAVfsBlI040cijP3IPtnEmKnmw9jX752wLCrNS5phEI44ZAq8i0SHrHrkZBIwdrbtRIM4l0jVfl3n4qLTI9tl4lyoi6H2zUi")
    # profile = graph.request('/me?fields=name,email')
    # print(profile)

    # b'{"obj":{"name":"Andrii Proniuk","id":"1683003735383969"}}
    raw_data = request.__dict__.get("COOKIES")
    req_data = request.__dict__
    # print(raw_data) ## no token
    # print(req_data) ## no token
    serializer_class = FBSocialAuthSerializer
    # print(request.user.is_authenticated)
    serializer = serializer_class()

    # getting user or exception while validating token
    result = serializer.validate_auth_token(auth_token)

    ###########################################
    raw_data = request.body
    print(raw_data)
    
    logger = logging.getLogger()
    # print(logger.handlers)

    # print(f"{request.META.get('messages')} - This is messages")
    # print(request.META)

    # x = traceback.extract_stack(f=None, limit=None)
    # print(x)

    # console_handler = logging.StreamHandler(stream=sys.stdout)
    # print(console_handler)

    exc = traceback.print_exc()
    # print(f'This is: {exc}')
    
    # sys.stdout.flush()
    # print(f'This is traceback: {x}')
    # traceback.print_stack(file=sys.stdout)
    # traceback.extract_stack()

    # print(f"This is requests: {requests.Session().__dict__.get('adapters')}")

    # print(f"This is session: {session}")

    session = requests.Session()
    print(f"This is session: {session}")


    adapters = requests.Session().__dict__.get('adapters')
    adapters = list(adapters.items())
    
    adapter1 = adapters[0]
    poolmanager = adapter1[1].__dict__.get('poolmanager')
    item = poolmanager.__dict__
    
    https = item.get('https')
    pools = item.get('pools').__dict__
    obj = pools.get('_container')
    print(obj.__dict__) ## empty

    adapter2 = adapters[1]

    retries=3
    backoff_factor=0.3
    status_forcelist=(500, 502, 504)
    

    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )

    adapter1 = HTTPAdapter(max_retries=retry)
    # httpAdapter = HTTPAdapter(pool_connections=10, pool_maxsize=100)

    # session.mount("https://graph.facebook.com:443")
    session.mount('http://', adapter1)
    
    print(session)

    sss = request.session
    print(sss.serializer.__dict__.get('__dict__'))


    # urlopen(method, url, body=None, headers=None, retries=None, redirect=True, assert_same_host=True, timeout=<object object>, pool_timeout=None, release_conn=None, chunked=False, body_pos=None, **response_kw)

    ###########################################################
    # print(result)
    if isinstance(result, dict):
        new_user_data = result

        ################################################
        print(new_user_data) ## +++
        # add register_social_user here
        ################################################

        messages.success(
            request,
            f'U\'ve just created the next user: {new_user.username} (^_-)≡☆'
        )
        return redirect ('/accounts/register-fbv/')
    
    if isinstance(result, CustomUser):
        # print(request.method) ## POST
        # print(result)

        # if not request.user == result:
        #     print(result)
        #     return redirect('accounts/check-user-auth/')
        #     # return redirect('/accounts/login-failed/')
        #     return render (request, 'user_status.html', context={'result': result})

        user = result
        login(request, user, backend='accounts.backends.EmailBackend')

        print(f"AUTHENTICATED: {user.is_authenticated}")
        print(user)

        ### google client id will be here: 'GOOGLE_CLIENT_ID': '1089815522327-308m9crjd7u9g4t5j7qsrhttef305l1a.apps.googleusercontent.com'
        # WSGI POST
        ## <Response status_code=200, "text/html; charset=utf-8">

        ### ***** ###
        # res = serializer.authenticate_social_user(request=request, user=user)
        # print(res)
        messages.success(
            request,
            f'U\'ve just successfully logined (^_-)≡☆;;;'
        )
        # print('dsd')
        # print(user)
        # return redirect('/accounts/login-success/')
        print(f'CustomUser: {user}')
        return render (request, 'accounts/snippets/fb_login.html', context={'user': user})
        # return render (request, 'accounts/snippets/fb_login.html', context={})


    return render (request, 'accounts/snippets/fb_login.html', context={'user': user})

class GoogleSocialAuthTemplateView(TemplateView, APIView):

    serializer_class = GoogleSocialAuthSerializer
    template_name = 'accounts/snippets/google_login.html'

    def get(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        return print(request.body)
        return print(request.__dict__)

    # def get_template_data(request):
    # def get(request, *args, **kwargs):
    #     try:
    #         print(request.__dict__)
    #         body = json.loads(request.body)
    #         print(body)
    #         return JsonResponse('Get data completed', safe=False)

    #     except Exception as err:
    #         print(err)
    #         pass

    # def perform_authentication(self, request):
    #     request2 = requests.Request()
    #     idinfo = id_token.verify_oauth2_token(
    #             auth_token, requests.Request()
    #         )

    # def get_context_data(self, request):
    #     body = json.loads(request.body)			
    #     return print(body)


        # print('This is request')
        #return print(request)

    # when realod a page
    # csrftoken=yKJeU0rKkUsxjaVxaBQCLuS8Hj7KicsrKKE880xaBpHSCdCOTC4LWvKLoIWEhAdR
    #           yKJeU0rKkUsxjaVxaBQCLuS8Hj7KicsrKKE880xaBpHSCdCOTC4LWvKLoIWEhAdR

# class TeamChartData(APIView):
#     # queryset = MyUser.objects.all()
#     # serializer_class = MyUserSerializer, #ProjectSerializer
#     permission_classes = [AllowAny]
#     http_method_names = ['get',]
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'accounts/oauth2_login.html'

#     def get_context_data(self, *args, **kwargs):
#         print(self.request.user)

# from django.urls import reverse_lazy
# from django.shortcuts import redirect
# def test_view(request):
#     return redirect ('/o/sighn-in-test/')

# @csrf_protect
# def social_authentication_view(request, *args, **kwargs):
#     '''
#         is a Google IdToken for user authnentication

#         :returns: Google IdToken
#         :rtype: str

#         .. note:: 
#             subsequent parameters: 
#                 * body: data sent by the client to our API
#                 * value: bytes from the body response
#                 * decoded_string: str data from bytes 
#                 * data: dict(), another way of getting IdToken 
#     '''
#     serializer_class = GoogleSocialAuthSerializer

#     # print(request.META.get('PATH_INFO'))
#     # print(f'{request.POST} This is post')
#     # print(request.META.get('GOOGLE_CLIENT_ID'))
#     # print(request.META.get('GOOGLE_CLIENT_SECRET'))
#     # print(request.META.get('data'))
#     # print(request)
    
#     # POST method is acquired via JS in a template
#     # print(request.META)
#     print(request.method)
#     try:
#         if request.method == 'POST':
#             print('This is POST')
#             # print(request.user.is_authenticated)
#             serializer = serializer_class()
#             # decoded_string = x.decode()
#             # print(decoded_string)
            

#             # 2 METHODS using JS POST fetch url
#             # get bytes API request
#             # value = request.body
#             # # from bytes to str dict data
#             # decoded_string = value.decode()
#             # token = eval(decoded_string).get('IdToken')

#             # another way of getting IdToken
#             # data = json.loads(request.body)
#             # print(data)
#             # token = data['IdToken']
            
#             # raw request method data
#             raw_data = request.__dict__.get('_body')
#             # print(f'{raw_data} this are bytes')
#             decoded_string = raw_data.decode()
#             # print(f'{decoded_string} this are decoded string1')
#             decoded_string = eval(decoded_string)
#             # print(f'{decoded_string} this are decoded string2')
#             token = decoded_string.get('IdToken')
#             # print(token)

#             # print(request.user.is_authenticated)
#             ## print(token) ## ++
            


#             result = serializer.validate_auth_token(token)
#             # print(request.user.is_authenticated)
#             # print(result) ## ++
#             # print(isinstance(result, CustomUser)) ## ++
            
#             # register user
#             if isinstance(result, dict):
                
#                 new_user_data = result
#                 print(new_user_data)
#                 ### ***** ###
#                 # new_user = serializer.register_social_user(new_user_data)
                
#                 messages.success(
#                 request,
#                 f'U\'ve just created the next user: {new_user.username} (^_-)≡☆'
#                 )
#                 return redirect ('/accounts/register-fbv/')
            
#             # login user
#             if isinstance(result, CustomUser):
#                 # print(request.method) ## POST
#                 # print(result)

#                 # if not request.user == result:
#                 #     print(result)
#                 #     return redirect('accounts/check-user-auth/')
#                 #     # return redirect('/accounts/login-failed/')
#                 #     return render (request, 'user_status.html', context={'result': result})

#                 user = result
#                 login(request, user, backend='accounts.backends.EmailBackend')
            
#                 # WSGI POST
#                 ## <Response status_code=200, "text/html; charset=utf-8">

#                 ### ***** ###
#                 # res = serializer.authenticate_social_user(request=request, user=user)
#                 # print(res)
#                 messages.success(
#                 request,
#                 f'U\'ve just successfully logined (^_-)≡☆;;;'
#                 )
#                 # print('dsd')
#                 # print(user)
#                 # return redirect('/accounts/login-success/')
#                 print(f'CustomUser: {user}')
#                 return redirect('/o/sighn-in-test/')
#                 # return render (request, 'accounts/oauth2_login.html', context={'user': user})
#                 # return redirect ('/panda-hardware/')
                    
#         if request.method == 'GET':
#             print(request.user)
#             # user = request.user
#             # print(f'GET: {user}')
#             context = {}
#             return render (request, 'accounts/oauth2_login.html', context)
    
#     except Exception as err:
#         print(err)