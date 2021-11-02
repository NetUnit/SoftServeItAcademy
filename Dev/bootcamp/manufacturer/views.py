from django.contrib.messages.api import error
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


############################## **** Create Manufacturer+Custom Validation **** ###############################
'''
    This view was made for self-development
    purposes in order to create custom validation

    attr correct_date_range: depicts a correct years range of the company foundation

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
    form = ManufacturerCreationForm(request.POST or None)

    # rendering various messages depend on user input
    if form.is_valid():
        manufacturer = form.save(commit=False)

        title = manufacturer.title
        year = manufacturer.year

        # min title length condition 
        min_title_length = len(title) > 1

        # dates range setup and retrieved date validation
        data = list(map(int, re.match(r"\d{4}-\d{2}-\d{2}", str(year)).group(0).split('-')))
        start_date = Dates.start_date
        end_date = Dates.end_date
        dates_1850_2021 = [ start_date + datetime.timedelta(n) for n in range(int ((end_date - start_date).days)) ]
        correct_date_range = datetime.date(data[0], data[1], data[2]) in dates_1850_2021
        print(Dates.start_date)

        if not correct_date_range:
            messages.error(request, f'{year} isn\'t correct year')
            return redirect ('/manufacturers/create/')

        if not min_title_length:
            messages.error(request, f'{title} isn\'t enough long')
            return redirect ('/manufacturers/create/')
        
        else:
            manufacturer.save()
            messages.success(request, f'U\'ve just added the next company: {title}')
            return redirect ('/manufacturers/create/')

    # fix this later (watch Denis video)
    # option that show's bad year input separately (apart of not valid form)
    try:
        year = form.cleaned_data.get('year')
        if year is None:
            #messages.error(request, f'{manufacturer.year} isn\'t correct')
            messages.error(request, f'Date input isn\'t correct')
            return redirect ('/manufacturers/create/')
    except:
        pass

    form = ManufacturerCreationForm()
    context = {'form': form}
    time.sleep(1.0)
    
    return render (request, 'manufacturer/create_manufacturer_form_crispy.html', context) #


############################## *** Datailed View + API *** ###############################
from .models import Manufacturer
def manufacturer_detailed_view(request, manufacturer_id, *args, **kwargs):
    '''
        Compare to the products app models were altered: 
        :return: manufacturer object or raise 404 status automatically when object is None
    '''
    manufacturer = Manufacturer.get_by_id(manufacturer_id)
    context = {'object': manufacturer}
    return render (request, 'manufacturer/detail.html', context)


def api_manufacturer_detailed_view(request, manufacturer_id, *args, **kwargs):
    manufacturer = Manufacturer.get_by_id(manufacturer_id)
    obj = manufacturer
    return JsonResponse({'id': obj.id, 'title': obj.title, 'country': obj.country, 'year': obj.year})


############################## *** Full List *** ###############################
def manufacturer_list_view(request, *args, **kwargs):
    try:
        qs = Manufacturer.get_all()
        context = {'manufacturer_list': qs}
        return render (request, 'manufacturer/list_main.html', context)
        #return render (request, 'manufacturer/manufacturer_list.html', context)
    except Exception as err:
        print(err)
        return False

############################## *** Update Product *** ###########################
# def manufacturer_update_view(request, manufacturer_id, *args, **kwargs):
#     try:
#         manufacturer = Manufacturer.get_by_id(manufacturer_id)
#         form = ManufacturerCreationForm(request.POST or None)
#         # return manufacturer # +++

#         #setup not required fields
#         for item in form.fields:
#             not_title = form.fields[item].required != 'title'
#             form.fields[item].required = False if not_title else 0

#         # geting attrs from the form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             country = form.cleaned_data.get('country')
#             year = form.cleaned_data.get('year')

#             # get data to write from a form
#             update_data = {
#                 'title': title,
#                 'country': country or None,
#                 'year': year or None
#                 }
#             manufacturer.__dict__.update(**update_data)
#             manufacturer.save()
#             messages.success(
#             request,
#             f'U\'ve just updated the next company: \'{manufacturer.title}\' (ﾉ･_-)☆'
#             )

#     except Exception as error:
#         print(error)

#     context = {'form': form}
#     return render (request, 'manufacturer/manufacturer_update_form_crispy.html', context)

@staff_member_required(login_url=f'/accounts/check-user-auth/')
def manufacturer_update_view(request, manufacturer_id, *args, **kwargs):
    try:
        form = ManufacturerCreationForm(request.POST or None)

        for item in form.fields:
            not_title = form.fields[item].required != 'title'
            form.fields[item].required = False if not_title else 0

        # geting attrs from the form
        if form.is_valid():
            title = form.cleaned_data.get('title')
            country = form.cleaned_data.get('country')
            year = form.cleaned_data.get('year')

            manufacturer = Manufacturer.update_by_id(
                manufacturer_id, title,
                country, year)
            
            messages.success(request,
                f'U\'ve just updated the next company: \n\
                \'{manufacturer.title}\' (ﾉ･_-)☆'
                )

    except Exception as error:
        print(error)

    context = {'form': form}
    return render (request, 'manufacturer/manufacturer_update_form_crispy.html', context)

############################## *** Update Product *** ###########################
@staff_member_required(login_url=f'/accounts/check-user-auth/')
def manufacturer_delete_view(request, manufacturer_id, *args, **kwargs):
    try:
        manufacturer = Manufacturer.get_by_id(manufacturer_id)
        Manufacturer.delete_by_id(manufacturer_id)
        messages.success(
            request, f'\'{manufacturer.title}\' has been removed'
        ) if True else 0
        #print(messages.__dict__)
        return redirect ('/manufacturers/list/')

    except Exception as err:
        print(err)
    

    