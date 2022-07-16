from products.models import Product
from .models import Manufacturer
from django.contrib.messages.api import error
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http.request import HttpRequest
from django.http import (
    HttpResponse,
    JsonResponse,
    Http404,
    HttpResponseRedirect
)
from manufacturer.forms import ManufacturerCreationForm

import time
from django.core.exceptions import ObjectDoesNotExist

# exception handling
from django.template import RequestContext
from django.contrib import messages

# *** path imports *** #
import pathlib
from wsgiref.util import FileWrapper
from mimetypes import guess_type


# *** Create Manufacturer + Custom Validation *** #
'''
    This views was made for self-development
    purposes in order to create custom validation

    attr correct_date_range: depicts a correct years range of the company
    foundation

    attr min_title_length: min length of the company title input

    try-except block: optionally shows input errors of a year
    attr year: automatically is required

    attrs start_date, end_date: may be customized in a separate file
'''
import re
import datetime
from manufacturer.dates_range import Dates
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required(login_url=f'/accounts/check-user-auth/')
def manufacturer_create_view(request, *args, **kwargs):
    form = ManufacturerCreationForm(
        request.POST or None,
        request.FILES or None
    )

    # rendering various messages depend on user input
    if form.is_valid():
        manufacturer = form.save(commit=False)

        title = manufacturer.title
        year = manufacturer.year

        # min title length condition
        min_title_length = len(title) > 1

        # dates range setup and retrieved date validation
        pattern = re.match(r"\d{4}-\d{2}-\d{2}", str(year)).group(0).split('-')
        data = list(map(int, pattern))
        start_date = Dates.start_date
        end_date = Dates.end_date
        dates_1850_2021 = [
            start_date + datetime.timedelta(n) for n in
            range(int((end_date - start_date).days))
        ]
        correct_date_range = datetime.date(
            data[0], data[1], data[2]) in dates_1850_2021

        if not correct_date_range:
            messages.error(
                request,
                f'{year} isn\'t correct year'
            )
            return redirect('/manufacturers/create/')

        if not min_title_length:
            messages.error(
                request,
                f'{title} isn\'t enough long'
            )
            return redirect('/manufacturers/create/')

        else:
            manufacturer.save()
            messages.success(
                request,
                f'U\'ve just added the next company: {title}'
            )
            return redirect('/manufacturers/create/')

    # fix this later (watch Denis video)
    # option that show's bad year input separately (apart of not valid form)
    try:
        year = form.cleaned_data.get('year')
        if year is None:
            messages.error(request, f'Date input isn\'t correct')
            return redirect('/manufacturers/create/')

    except BaseException:
        pass

    form = ManufacturerCreationForm()
    context = {'form': form}
    return render(
        request,
        'manufacturer/create_manufacturer_form_crispy.html',
        context
    )


# *** Datailed View + API *** #
def manufacturer_detailed_view(request, manufacturer_id, *args, **kwargs):
    '''
    Compare to the products app models were altered:
    :returns: manufacturer object or raise 404 status
              automatically when object is None
    '''
    manufacturer = Manufacturer.get_by_id(manufacturer_id)
    context = {'manufacturer': manufacturer}
    return render(request, 'manufacturer/detail.html', context)


def api_manufacturer_detailed_view(request, manufacturer_id, *args, **kwargs):
    manufacturer = Manufacturer.get_by_id(manufacturer_id)
    obj = manufacturer
    return JsonResponse(
        {'id': obj.id,
         'title': obj.title,
         'country': obj.country,
         'year': obj.year
         }
    )


# *** Full List *** #
def manufacturer_list_view(request, *args, **kwargs):
    qs = Manufacturer.get_all()
    context = {'manufacturer_list': qs}
    return render(request, 'manufacturer/list_main.html', context)


# *** Full Product List Specified By Company *** #
def get_products_manufacturer(request, manufacturer_id, *args, **kwargs):
    manufacturer = Manufacturer.get_by_id(manufacturer_id)
    products = manufacturer.products.all()
    context = {'products': products}
    return render(
        request,
        'manufacturer/products_manufacturer.html',
        context
    )


# *** Company Update View *** #
@staff_member_required(login_url=f'/accounts/check-user-auth/')
def manufacturer_update_view(request, manufacturer_id, *args, **kwargs):

    form = ManufacturerCreationForm(
        request.POST or None,
        request.FILES or None
    )

    for field in form.fields:
        form.fields[field].required = False

    # geting attrs from the form
    manufacturer = Manufacturer.get_by_id(manufacturer_id)

    if form.is_valid():
        title = form.cleaned_data.get('title')
        country = form.cleaned_data.get('country')
        year = form.cleaned_data.get('year')
        image = form.cleaned_data.get('image')
        media = form.cleaned_data.get('media')
        print(image, media)

        manufacturer = Manufacturer.update_by_id(
            manufacturer_id, title,
            country, year,
            image, media
        )

        messages.success(
            request,
            f'U\'ve just updated the next company: \n\
            \'{manufacturer.title}\' (ﾉ･_-)☆'
        )

    context = {'form': form}
    return render(
        request,
        'manufacturer/manufacturer_update_form_crispy.html',
        context
    )


# *** Company Delete View *** #
@staff_member_required(login_url=f'/accounts/check-user-auth/')
def manufacturer_delete_view(request, manufacturer_id, *args, **kwargs):

    manufacturer = Manufacturer.get_by_id(manufacturer_id)
    Manufacturer.delete_by_id(manufacturer_id)
    messages.success(
        request, f'\'{manufacturer.title}\' has been removed'
    ) if True else 0
    return redirect('/manufacturers/list/')


def media_download_view(request, manufacturer_id, *args, **kwargs):
    '''
    downlodas media of a certain company manufacturer
    :returns: HttpResponse in the form of a downloading file
                (as oppose to render or redirect a new page)
    '''
    manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)

    media = manufacturer.media
    if not media:
        raise Http404

    manufacturer_path = media.path
    path = pathlib.Path(manufacturer_path)

    if not path.exists():
        raise Http404

    # file extension
    ext = path.suffix
    file_name = f'panda-moto-manufacturer-{manufacturer_id}{ext}'

    with open(path, 'rb') as file:
        wrapper = FileWrapper(file)
        content_type = 'application/force-download'
        first_type = 0
        guessed_ = guess_type(path)[first_type]
        content_type = guessed_ if guessed_ else content_type
        response = HttpResponse(wrapper, content_type=content_type)
        response['Content-Disposition'] = f'attachment;filename={file_name}'
        response['X-SendFile'] = f'{file_name}'
        return response
