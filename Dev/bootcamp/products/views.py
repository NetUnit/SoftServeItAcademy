from django.http import request
from .models import Product, Manufacturer
from django.contrib import messages
from products.forms import ProductCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http.request import HttpRequest
from django.http import (
    HttpResponse,
    JsonResponse,
    Http404,
    HttpResponseRedirect
)
# Class-based View for list of objects
from django.views.generic import ListView

import time
# *** Exception Handling *** #
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.forms import ValidationError
from django.utils.translation import gettext as _
from django.template import RequestContext

# *** Django Generic HomePageView *** #
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import SuspiciousFileOperation

# *** path imports *** #
import pathlib
from wsgiref.util import FileWrapper
from mimetypes import guess_type
import os

# *** auth user model *** #
from django.contrib.auth import get_user_model

# *** exceptions *** #
from django.template import RequestContext
# from rest_framework import status


# *** Class-based TemplateView for panda homepage *** #
class HomePageView(TemplateView):
    template_name = "home.html"


# *** product detailed view *** #
# using python simple function get(pk=pk)
# dynamic id from url + error handling method#1
def product_detailed_view(request, product_id, *args, **kwargs):
    try:
        # ex1: get product object with django shortcut
        product = get_object_or_404(Product,  pk=product_id)
        image = product.image

        # ex2: django abstarct ddl/dml queries to db
        product = Product.objects.get(pk=product_id)

        # ex3: using filter
        # product = Product.objects.filter(pk=product_id).first()
    except Product.DoesNotExist:
        # this would render html page with HTTP status code
        raise Http404(u'Product wasn\'t found')

    context = {'product': product, 'image': image}
    return render(request, 'products/detail.html', context)


# JSON response of product#2 # example just for url
def api_product_detailed_view(request, product_id, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404
        # will return JSON response with HTTP status code 404
        # return JsonResponse({"message": "Not found"}, status=404)
    return JsonResponse({'id': obj.id, 'title': obj.title,
                         'content': obj.content, 'price': obj.price})


# *** Product Create View *** #
def product_list_view(request, *args, **kwargs):
    products = Product.get_all()
    images = [str(product.image) for product in products]
    context = {'product_list': products, 'images': images}
    return render(request, 'products/list_main.html', context)


# *** Full List *** #
# get the list of items in every object
# will get the list of all individual instances of this model
def product_list_view2(request, *args, **kwargs):
    try:
        # gets queryset of objects
        qs = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404
    context = {'object_list': qs}
    return render(request, 'products/list.html', context)


class ProductListView(ListView):
    model = Product
    paginate = 10
    # in case of model meta class doesn't possess ordered list
    # model.objects.all().order_by('id')
    model.objects.all()


# *** Test Viewv for Methods *** #
def method_view(request, *args, **kwargs):
    '''
    test possbilities of various djnago features
    rendered as a context output into browser
    '''
    result1 = (f'Django request dict: {request.GET} | ' +
               'python standart dict: {dict(request.GET)}')
    result2 = (f'Django request dict: {request.POST} | ' +
               'python standart dict: {dict(request.POST)}')
    result3 = request.method == 'GET'
    result4 = request.method == 'POST'
    context = {'result1': result1, 'result2': result2,
               'result3': result3, 'result4': result4}
    return render(request, 'methods.html', context)


# **** Create + Validation Form **** #
@staff_member_required(login_url=f'/accounts/check-user-auth/')
def product_create_view(request, *args, **kwargs):
    '''
    user_id not grabbed from the url, but instatly taken from the
    request session and written to the db (as a primary key)
    field manufacturers are manually added to the intermediate table
    through models add() method

    ..note: backend placeholders used in the ProductCreationForm
            along with field validation
    '''
    try:
        form = ProductCreationForm(
            request.POST or None,
            request.FILES or None
        )

        # raises ValidationError when no manufacturers provided
        form.check_manufacturers()

        if form.is_valid():
            form.check_title()
            data = form.cleaned_data
            print(f'This is product data from HTML: {data}')
            product = Product.create(**data)
            product.user = request.user
            product.save()
            messages.success(
                request,
                f'U\'ve just created the next product: {product.title} (^_-)≡☆'
                )
            return redirect('/products/create/')

        messages.error(
                request,
                f'Please make sure to select all fields（♯××）┘ ◎☆')

        form = ProductCreationForm()
        context = {'form': form}
        return render(
            request,
            'products/create_product_form_as_crispy_fields.html',
            context
        )

    except ValidationError as error:
        LOGGER.warning(f'{error}')
        return render(request, 'form_failure.html',
                      context={'form_error': ''.join(error)})


@staff_member_required(login_url=f'/accounts/check-user-auth/')
def product_update_view(request, product_id,  *args, **kwargs):

    form = ProductCreationForm(
        request.POST or None,
        request.FILES or None
    )

    for field in form.fields:
        form.fields[field].required = False

    if form.is_valid():
        data = form.cleaned_data
        product = Product.update_by_id(product_id, data)

        messages.success(request, f'U\'ve just updated the next company: \n\
        \'{product.title}\' (ﾉ･_-)☆')

    context = {'form': form}
    return render(
        request,
        'products/product_update_form_as_crispy_fields.html',
        context
    )


@staff_member_required(login_url=f'/accounts/check-user-auth/')
def product_delete_view(request, product_id, *args, **kwargs):
    product = Product.get_by_id(product_id)
    Product.delete_by_id(product_id)
    messages.success(request, f'\'{product.title}\' has been removed') if True else None
    return redirect('/products/list/')


def media_download_view(request, product_id, *args, **kwargs):
    '''
        downlodas media of a certain product
        :returns: HttpResponse in the form of a downloading file
                  (as oppose to render or redirect a new page)
    '''
    product = Product.get_by_id(product_id)
    image = product.image
    if not image:
        raise Http404

    product_path = image.path
    path = pathlib.Path(product_path)

    if not path.exists():
        raise Http404

    # file extension
    ext = path.suffix
    file_name = f'panda-moto-product-{product_id}{ext}'

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
