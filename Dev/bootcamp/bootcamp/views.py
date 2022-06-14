'''
if views are any more complicated than that we can put those
here ($ for example they need their own models or forms or ...)
'''
from django.shortcuts import render, redirect
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _
from django.contrib import messages
from products.models import Product
from manufacturer.models import Manufacturer
import time
from bootcamp.settings import LOGGER
from bootcamp.forms import ProcessContactForm

# *** RequestContext imports *** #
from django.template import RequestContext, Template


# *** Panda Hardware info-page *** #
def panda_link_view(request, *args, **kwargs):
    return render(request, 'about_us.html', context={})


# *** Custom Error Pages *** #
def handler404(request, exception, *args, **kwargs):
    context = {'exception': exception}
    response = render(request, '404.html', context)
    response.status = 404
    return response


def handler500(request, *args, **kwargs):
    context = {}
    response = render(request, '500.html', context)
    response.status = 500
    return response


def handler400(request, exception, *args, **kwargs):
    # HttpResponseBadRequest == 400
    context = {}
    response = render(request, '400.html', context)
    response.status = 400
    return response


def handler403(request, exception, *args, **kwargs):
    # PermissionDenied == 403
    context = {'exception': exception}
    response = render(request, '403.html', context)
    response.status = 403
    return response


# this part of a view get main logic from  a model
def search_venues(request, *args, **kwargs):
    # match logic
    # add logic to extend search by 4 letters in a raw
    if request.method == "POST":

        searched = request.POST.get('searched')
        # convert user_input to lowercase and split to a single word
        lowercase_and_split = lambda *args: (
            ' '.join(list(map(str, args))).lower().split())
        # convert db_field to lowercase and split to a single word
        lowercase_and_list = lambda *args: (
            ' '.join([' '.join(i) for i in args]).lower().split())
        user_input = lowercase_and_split(searched)
        all_prod = Product.get_all()
        all_manuf = Manufacturer.get_all()
        product_fields = [
            dict(obj.__dict__).get('title') for obj in all_prod
        ]
        manufacturer_fields = [
            dict(obj.__dict__).get('title') for obj in all_manuf
        ]

        db_fields = product_fields + manufacturer_fields
        match = [
            word for word in user_input if word in lowercase_and_list(db_fields)
        ]
        matched_items = list()

        for obj in Product.get_all() + Manufacturer.get_all():
            for word in match:
                if word.capitalize() in obj.__dict__.get('title'):
                    matched_items.append(obj)

        matched_items = list(set(matched_items))

        context = {'searched': searched, 'objects_list': matched_items,
                   'obj_prod_filter': all_prod,
                   'obj_man_filter': all_manuf}

        if any(matched_items):
            messages.success(
                request,
                f'☆彡(ノ^ ^)ノ Congrat\'s ヘ(^ ^ヘ)☆彡 Item\'s found'
            )
            return render(
                request,
                'products/search_venues.html', context
            )

        else:
            messages.success(request, '¯\_(⊙︿⊙)_/¯ Nothing has been found')
            return render(request, 'products/search_venues.html', context)


# search widget withjout form
# works but show only messages
def search_view(request, *args, **kwargs):

    objects = Manufacturer.get_all() + Product.get_all()

    if request.method == 'POST':
        item = request.POST.get('searched')

        for obj in objects:
            # we're gonna filter db manually to find matches by words
            object_words = ' '.join(
                [str(i) for i in list(obj.__dict__.values())]
            )
            object_attrs = list(obj.__dict__.values())
            object_found = item in object_words or item in object_attrs
            min_length = len(item) > 1

            if object_found:
                messages.success(request, f'{obj}')
                time.sleep(0.25)
                return redirect('/search/')

            if not min_length:
                messages.error(request, f'Oh wov. It\'s definitely too short {item}')
                return redirect('/search/')

        else:
            messages.error(request, f'Nothing has been found through: {item}')
            time.sleep(0.25)
            return redirect('/search/')

    storage = messages.get_messages(request)
    return render(request, 'products/search_messages.html')


# *** feedback form for middleware *** #
def feedback_form_view(request, *args, **kwargs):
    form = ProcessContactForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        feedback = form.cleaned_data.get('feedback')
        messages.success(request, 'Many thanks. We appreciate your feedback')
        # *** !!! FOR LATER !!! ***
        # add transfer message with POST data to admin email
        return redirect('/feedback/')

    form = ProcessContactForm()
    context = {'form': form}
    return render(request, 'accounts/feedback_form_as_p.html', context)


def ip_address_processor(request):
    return {"ip_address": request.META.get('REMOTE_ADDR')}


def test_request_context_view(request, *args, **kwargs):
    '''
    Django comes with a special Context class, django.template.RequestContext,
    which works a little differently than the usual django.template.Context.
    It accepts HttpRequest as the first arg.
        For example:

        c = RequestContext(request, {
            'foo': 'bar',
        })
    The second thing is it automatically fills the context with several variables
    according to the context_processors engine configuration option.
    '''
    # instantiating template obj
    template = Template(
        'User: {{ username }} | Email: {{ email }} | IP: {{ ip_address }}'
    )

    request_context = RequestContext(
        request,
        {'username': 'User: ',
            'email': 'Email: ',
            'ip_address': 'IP: '},
        # assign 3rd positional arg to Req Context
        [ip_address_processor])

    # assign var username to request context
    request_context.push({'username': "NetUnit"})
    # assign var email to request context
    request_context.push({'email': "andriyproniyk@gmail.com"})
    return HttpResponse(template.render(request_context))
