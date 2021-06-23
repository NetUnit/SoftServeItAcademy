from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.http.request import HttpRequest
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from manufacturer.forms import ManufacturerCreationForm

import time
from django.core.exceptions import ObjectDoesNotExist

# exception handling
from django.template import RequestContext
from django.contrib import messages

def manufacturer_create_view(request, *args, **kwargs):
    form = ManufacturerCreationForm(request.POST or None)

    if form.is_valid():
        manufacturer = form.save(commit=False)
        
        min_title_length = len(str(form.cleaned_data.get('title'))) > 1
        # print(min_title_length)
        if min_title_length:
            manufacturer.save()
            messages.success(request, f'{manufacturer.title}')
            return redirect ('/manufacturers/create/')
        else:
            get_title = form.cleaned_data.get('title')
            messages.error(request, f'{get_title} isn\'t enough long')
            return redirect ('/products/create/')

    form = ManufacturerCreationForm()
    context = {'form': form}
    time.sleep(1.0)
    
#    return render (request, 'forms.html', context) # +
#     # return render (request, 'products/create_product_input_tags.html', context) # +
#     ## !!required fields demand!!
#     # return render (request, 'products/create_product_form_as_p.html', context) # +
    return render (request, 'products/create_product_form_as_crispy_fields.html', context) # +
#    return render (request, 'products/create_product_form_crispy.html', context) # +

# def manufacturer_list_view(request):
#     pass