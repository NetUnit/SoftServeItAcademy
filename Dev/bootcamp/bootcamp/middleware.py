
from django.core.exceptions import PermissionDenied
from django.http.response import Http404
from django.http.response import HttpResponseBadRequest

import datetime
from django.core.cache import cache
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

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

    # def process_exception(self, request, exception):
    #     if isinstance(exception, Http404):
    #         message = f"""
    #             {exception.args},
    #             User: {request.user},
    #             Referrer: {request.META.get('HTTP_REFERRER', 'no referrer')}
    #         """
    #         exception.args = (message,)
            

        