from rest_framework import generics, viewsets, mixins, permissions
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q

from accounts.models import CustomUser
from django.contrib.auth import authenticate, login
from rest_framework import serializers

from .serializers import (
    CustomUserCreateSerializer,
    CustomUserLoginSerializer,
    GoogleSocialAuthSerializer
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

    template = 'accounts/oauth2_login.html'
    serializer_class = GoogleSocialAuthSerializer
    # renderer_classes = [TemplateHTMLRenderer, template]


    def post(self, request, *args, **kwargs):
        '''
            posted data from google with auth_token & auth_token_id

        '''
        # serializer = GoogleSocialAuthSerializer()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data.get('auth_token')
        return Response(data, status=status.HTTP_200_OK)
    


from django.views.generic import TemplateView
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages


# class CustomLoginView(auth_views.LoginView):
#     form_class = LoginForm
#     template_name = 'accounts/login_form_as_p.html'

# @csrf_exempt
@csrf_protect
def social_authentication_view(request, *args, **kwargs):
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
        serializer = serializer_class()

        try:
            # get bytes API request
            value = request.body
            # from bytes to str dict data
            decoded_string = value.decode()
            token = eval(decoded_string).get('IdToken')
            
            # another way of getting IdToken
            # data = json.loads(request.body)
            # print(data)
            # token = data['IdToken']

            result = serializer.validate_auth_token(token)
            # print(result) ## ++
            # print(isinstance(result, CustomUser)) ## ++

            if isinstance(result, dict):
                new_user_data = result
                new_user = serializer.register_social_user(new_user_data)
                messages.success(
                request,
                f'U\'ve just created the next user: {new_user.username} (^_-)≡☆'
                )
                return redirect ('/accounts/register-fbv/')
            
            if isinstance(result, CustomUser):
                print(result)
                user = result
                res = serializer.authenticate_social_user(request=request, user=user)
                print(res)

                messages.success(
                request,
                f'U\'ve just successfully logined (^_-)≡☆'
                )
                return redirect('/')

        except Exception as err:
            print(err)
        
        return render (request, 'accounts/oauth2_login.html', context={})
        # return redirect ('/o/sighn-in-test/')

    return render (request, 'accounts/oauth2_login.html', context={})



class GoogleSocialAuthTemplateView(TemplateView, APIView):

    serializer_class = GoogleSocialAuthSerializer
    template_name = 'accounts/oauth2_login.html'

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