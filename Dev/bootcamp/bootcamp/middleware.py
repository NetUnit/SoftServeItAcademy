from django.core.exceptions import PermissionDenied
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest

import datetime
from django.core.cache import cache
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from bootcamp.hosts import Hosts
from django.contrib import messages
from django.shortcuts import render, redirect

class CustomExceptionMiddleware(MiddlewareMixin):

    # def process_request(self, request):
    #     current_user = request.user
    #     if request.user.is_authenticated:
    #         now = datetime.datetime.now()
    #         cache.set('seen_%s' % (current_user.username), now, 
    #                        settings.USER_LASTSEEN_TIMEOUT)
    
    def process_exception(self, request, exception):
        # print(f"This is given exception: {exception}")
        if isinstance(exception, Http404):
            message = f'{exception}'
            exception.args = (message,)
        
        if isinstance(exception, PermissionDenied):
            message = f'{exception}'
            exception.args = (message, )

    def process_request(self, request):
       
        try:
            x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
            remote_addr = request.META.get('REMOTE_ADDR')
            # link = request.META.get('HTTP_REFERER')
            if x_forward:
                ip = x_forward.split(',')[0]            
            else:
                ip = remote_addr 

            banned_networks = Hosts()
            localhost = ['127']
            network = ip.split('.')[0]
            if network in banned_networks._restricted:
                messages.info(request,
                    ('Unfortunately this content is not' +
                    'available in your country')
                )
                # return redirect('/access-status/')
                return render(request, 'access_status.html', context={})
            # if network in localhost:
            #     messages.info(request,
            #         'This is a localhost'
            #     )
            #     # return redirect('/access-status/')
            #     return render(request, 'access_status.html', context={})
        except:
            pass