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


####################  *** get app name *** ########################
def footer_app_name(request, *args, **kwargs):
    return {
        'app_name_0': settings.MAIN_PAGE,
        'app_name_0_tagline': settings.MAIN_PAGE_TAGLINE,
        'app_name_1': settings.APP_NAME_1,
        'app_name_1_tagline': settings.APP_NAME_1_TAGLINE,
        'app_name_2': settings.APP_NAME_2,
        'app_name_2_tagline': settings.APP_NAME_2_TAGLINE,
        'app_name_3': settings.APP_NAME_3,
        'app_name_3_tagline': settings.APP_NAME_3_TAGLINE,
        'app_name_4': settings.APP_NAME_4,
        'app_name_4_tagline': settings.APP_NAME_4_TAGLINE,
        'app_name_5': settings.APP_NAME_5,
        'app_name_5_tagline': settings.APP_NAME_5_TAGLINE,
    }


####################  *** get root path *** #########################
def root(request, *args, **kwargs):
    return {
        'root': request.path
    }


def detailed_method(request, *args, **kwargs):
    return {
        'method': settings.METHOD,
    }


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
####################  *** get app_name from urls.py *** #########################
# from products.urls import app_name as product_app

## disabled --->
# def get_app_from_urls(request, *args, **kwargs):
#     return {
#         'app_info_1': product_app
#     }