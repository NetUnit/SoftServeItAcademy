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

def some_middleware_view(request, get_response, *args, **kwargs):
    return print(f'{get_response}')

################# *** Panda Hardware *** ###################
def panda_link_view(request, *args, **kwargs):
    return render(request, 'about_us.html', context={})
    # return HttpResponse('<h2> This is Panda website: add here info about the website </h2>')

################ *** Custom Error Pages *** #################
def handler404(request, exception, *args, **kwargs):
    # Http404 == 404
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
    
################ *** Custom Error Pages *** #################
# def feedback_form_view(request, *args, **kwargs):
#     print(request.POST.__dict__)
#     form = ProcessContactForm(request.POST or None)
#     print(form.is_valid())
#     #print(form.__dict__)
#     if form.is_valid():
#         form_data = form.cleaned_data
#         context = {'form_data': form}
#         return render(request, 'feedback_form_as_p.html', context)

#     form = ProcessContactForm()
#     context = {'form_data': form}
#     return render(request, 'feedback_form_as_p.html', context)

# rebuild search view --> get itme from all tables
############################## **** Search View **** ###############################
# this part of a view contains logic itself
# def search_venues(request, *args, **kwargs):

#     if request.method == "POST":
#         searched = request.POST.get('searched')
#         print(searched)

#         objects_prod = Product.get_all()
#         objects_man = Manufacturer.get_all()
        
#         ## will get an object from the db based on the word separately + case insensitive
#         filter_model = lambda model: [
#             obj for obj in model if searched.lower() in ' '.join([str(attr).lower() for attr in list(obj.__dict__.values())])
#             ]
#         obj_man_filter = filter_model(objects_prod)
#         obj_prod_filter = filter_model(objects_man)

#         objects_list = obj_man_filter + obj_prod_filter

#         # print(objects_list)
#         # print(obj_man_filter)
#         # print(obj_prod_filter)
        
#         # alternatively
#         # filter_product = Product.objects.filter(name__contains=searched)
#         # print(filter_product)
        
#         context = {
#             'searched': searched,
#             'objects_list': objects_list,
#             'obj_prod_filter': obj_prod_filter,
#             'obj_man_filter': obj_man_filter
#             }
    
#         if any(objects_list):
#             messages.success(request, f'☆彡(ノ^ ^)ノ Congrat\'s ヘ(^ ^ヘ)☆彡 Item\'s found')
#             return render (request, 'products/search_venues.html', context)

#         else:
#             print('fuck')
#             messages.success(request, '¯\_(⊙︿⊙)_/¯ Nothing has been found')
#             return render (request, 'products/search_venues.html', context)
        
# this part of a view get main logic from  a model
def search_venues(request, *args, **kwargs):
   ## match logic add to extend by 4 letters in a raw
    if request.method == "POST":
        print(request.POST)
        searched = request.POST.get('searched')

        # convert user_input to lowercase and split to a single word
        lowercase_and_split = lambda *args: (
            ' '.join(list(map(str, args))).lower().split())

        # # convert db_field to lowercase and split to a single word
        lowercase_and_list = lambda *args: (
            ' '.join([' '.join(i) for i in args]).lower().split())

        # db_fields = Product.get_all() + Manufacturer.get_all()
        # [Product(id=1), Product(id=2), Product(id=3), Product(id=4)]
        
        user_input = lowercase_and_split(searched)

        all_prod = Product.get_all()
        all_manuf = Manufacturer.get_all()

        ## ['Raspberry Pi', 'Turing Pi', 'PocketBeagle', 'Pine64']
        product_fields = [dict(obj.__dict__).get('title') for obj in all_prod]
        
        ## ['Sony', 'Octavo Systems']
        manufacturer_fields = [dict(obj.__dict__).get('title') for obj in all_manuf]
        
        # create method id model to cover this
        db_fields = product_fields + manufacturer_fields

        match = [word for word in user_input if word in lowercase_and_list(db_fields)]

        matched_items = list()

        for obj in Product.get_all() + Manufacturer.get_all() :
            for word in match: # match --->  user input
                if word.capitalize() in obj.__dict__.get('title'):
                    matched_items.append(obj)

        matched_items = list(set(matched_items))
    
        context = {
            'searched': searched,
            'objects_list': matched_items,
            'obj_prod_filter': all_prod,
            'obj_man_filter': all_manuf
            }
    
        if any(matched_items):
            messages.success(request, f'☆彡(ノ^ ^)ノ Congrat\'s ヘ(^ ^ヘ)☆彡 Item\'s found')
            return render (request, 'products/search_venues.html', context)

        else:
            messages.success(request, '¯\_(⊙︿⊙)_/¯ Nothing has been found')
            return render (request, 'products/search_venues.html', context)


# ## search widget with form
# from products.forms import ItemSearchForm
# def search_view(request, *args, **kwargs):
    
#     form = ItemSearchForm(request.POST or None)

#     print(form.is_valid())

#     if form.is_valid():
#         min_title_length = len(str(form.cleaned_data.get('searched'))) > 1
#         print(min_title_length)
#         if min_title_length:
            
#             searched = form.cleaned_data.get('searched')
#             messages.success(request, f'{searched}')
            
#             # зробити логіку яка буде брати класметод з моделі: пошук по параметрах (title, country, year)
            


#             return redirect ('/search/')
#         else:
#             get_title = form.cleaned_data.get('searched')
#             messages.error(request, f'{get_title} isn\'t enough long')
#             return redirect ('/search/')
    

#     form = ItemSearchForm()
#     context = {'form': form}
#     time.sleep(0.01)
#     return render (request, 'products/search_messages.html', context)

# search widget withjout form
# works but show only messages
def search_view(request, *args, **kwargs):

    objects = Manufacturer.get_all() + Product.get_all()
    
    if request.method == 'POST':
        item = request.POST.get('searched')

        for obj in objects:
            
            # we're gonna filter database manually to find matches by words 
            object_words = ' '.join([str(i) for i in list(obj.__dict__.values())])
            object_attrs = list(obj.__dict__.values())
            object_found = item in object_words or item in object_attrs
            min_length = len(item) > 1
            
            if object_found:
                messages.success(request, f'{obj}')
                time.sleep(0.25)
                return redirect ('/search/')

            if not min_length:
                messages.error(request, f'Oh wow. It\'s definitely too short {item}')
                return redirect ('/search/')
    
        else:
            messages.error(request, f'Nothing has been found through: {item}')
            time.sleep(0.25)
            return redirect ('/search/')
    
    storage = messages.get_messages(request)
    # storage = storage.__dict__['storages']
    # print(storage[0].__dict__['signer'].__dict__)
    return render (request, 'products/search_messages.html')
 
#################### *** feedback form for middleware *** ####################
def feedback_form_view(request, *args, **kwargs):
    form = ProcessContactForm(request.POST or None)
    # print(form.is_valid())
    if form.is_valid():
        email = form.cleaned_data.get('email')
        feedback = form.cleaned_data.get('feedback')
        messages.success(request, 'Many thanks. We appreciate your feedback')
        ## add transfer message with POST data to admin email
        return redirect('/feedback/')

    form = ProcessContactForm()
    context = {'form': form}
    return render (request, 'accounts/feedback_form_as_p.html', context)



# ### work +++ 
# def search_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         searched = request.POST.get('searched')
#         #print(request.POST)
#         #print(len(searched))

#         if len(searched) > 0:
#             context = {'searched': searched}
#             return render (request, 'products/search2_simple.html', context)

#         else:
#             searched = 'Data does not exist'
#             context = {'searched': searched}
#             return render (request, 'products/search2_simple.html', context)

#     else:
#         messages.error(request, f'make sure U r entering searched data in the correct order')


#     return render (request, 'products/search2_simple.html', context = {})


# # form +++ (doesn't work)
# def search_view(request, *args, **kwargs):
#     system_messages = messages.get_messages(request)
#     # print(list(messages.get_messages(request)))
#     print(request.method)
#     # # manuafcturer section from DB
#     # manufacturer_qs = Manufacturer.get_all()
#     # print(manufacturer_qs)
#     # context = {'manufacturer_list': manufacturer_qs }
#     # #return render (request, 'products/search.html', context)
    
#     # # product section from DB
#     # product_qs = Product.get_all()
#     # print(product_qs)
#     # context = {'manufacturer_list': manufacturer_qs }
#     # return render (request, 'products/search.html', context)

#     # keyword = request.POST.get('keyword')
#     # print(keyword)

#     # getting keyword from 
#     # try:
#     #     item = request.POST.__dict__
#     #     print(item)
#     # except:
#     #     pass

#     # form = ItemSearchForm(request.POST or None)
#     # #keyword = form.cleaned_data.get('keyword')
#     # #print(keyword)
#     # print(form.is_valid())
#     # if form.is_valid():
#     #     keyword = form.cleaned_data.get('keyword')
#     #     context = {'keyword': keyword}
#     #     return render (request, 'products/search.html', context)
#     # pass
    

# def search_view(request, *args, **kwargs):
    # if request.method == 'POST':
    #     searched = request.POST.get('searched')
    #     print(searched)
    #     messages.add_message(request, messages.INFO, 'U searched for: ')
    #     context = {'searched': searched}
    #     #messages.clear()
        
    # else:
    #     time.sleep(0.5)
    #     messages.error(request, 'There is no such item in the database')
    #     return redirect ('/search/')

    # storage = messages.get_messages(request)
    # for _ in storage:
    #     pass

    # return render (request, 'products/search_messages.html', context)

# def product_create_view(request, *args, **kwargs):
#     form = ProductCreationForm(request.POST or None)

#     if form.is_valid():
#         product = form.save(commit=False)
        
#         min_title_length = len(str(form.cleaned_data.get('title'))) > 1
#         # print(min_title_length)
#         if min_title_length:
#             product.save()
#             messages.success(request, f'{product.title}')
#             return redirect ('/products/create/')

#     form = ProductCreationForm()
#     context = {'form': form}
#     time.sleep(1.0)
    
# #    return render (request, 'forms.html', context) # +
# #     # return render (request, 'products/create_product_input_tags.html', context) # +
# #     ## !!required fields demand!!
# #     # return render (request, 'products/create_product_form_as_p.html', context) # +
# #     # return render (request, 'products/create_product_form_as_crispy_fields.html', context) # +
#     return render (request, 'products/create_product_form_crispy.html', context) # +

