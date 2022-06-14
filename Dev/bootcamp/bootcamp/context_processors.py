"""bootcamp URL Configuration

The context_processor file serves to crete our own Python function
(Context Processor), that will be added to pre-build Django batteries,
in order to render customized HTML data
"""
from django.conf import settings


# *** custom context_processor *** #
def products(request, *args, **kwargs):
    '''
    :request: HttpRequest object
    :returns: dictionary that gets added to the request context
              of products app
    '''
    return {
        'products_group': settings.PRODUCTS_GROUP,
        'products_tagline': settings.PRODUCTS_TAGLINE
    }


#  *** get app name context *** #
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
        'company_name_tagline': settings.COMPANY_NAME_TAGLINE,
    }


# *** get root path *** #
def root(request, *args, **kwargs):
    return {
        'root': request.path
    }
