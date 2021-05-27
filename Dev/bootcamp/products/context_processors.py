"""bootcamp URL Configuration

The context_processor file serves to crete our own Python function (Context Processor),
that will be added to pre-build Django batteries, in order to render customized HTML data
"""


from django.conf import settings


##################### *** custom context_processor *** #########################

def products(request, *args, **kwargs):
    return {
        'products_group': settings.PRODUCTS_GROUP,
        'products_tagline': settings.PRODUCTS_TAGLINE
    }



#####################  *** get app name *** #########################
## disabled ---> manual setting
# def root(request, *args, **kwargs):
#     return {
#         'root': settings.ROOT_PAGE,
#         'root_tagline': settings.ROOT_TAGLINE
#     }


## disabled ---> auto setting through getting the name of app
# from django.urls import (get_resolver, get_urlconf, resolve, reverse, NoReverseMatch)


# def appname(request):
#     return {'app_name': resolve(request.path).app_name}


# def context_appname(request):
#     return {
#         'app_name': request.resolver_match.app_name
#     }

# def resolver_context_processor(request):
#     return {
#         'app_name': request.resolver_match.app_name,
#         'namespace': request.resolver_match.namespace,
#         'url_name': request.resolver_match.url_name
#     }
########################################################################
