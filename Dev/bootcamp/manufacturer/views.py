from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Manufacturer
from .forms import ManufacturerCreationForm
# from manufacturer import manufacturers_list

from django.contrib import messages

import time


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
            return redirect ('/manufacturers/create/')

    form = ManufacturerCreationForm()
    context = {'form': form}
    time.sleep(1.0)

    return render (request, 'manufacturer/create_manufacturer_crispy_form.html', context)

# def manufacturer_list_view(request):
#     pass