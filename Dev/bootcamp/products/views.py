from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.http.request import HttpRequest
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from .models import Product, Manufacturer
import time
from django.core.exceptions import ObjectDoesNotExist

# exception handling
from django.template import RequestContext


################# *** Django Generic HomePageView *** #############
from django.views.generic import TemplateView, ListView # Import TemplateView

## main page
## Class-based View
class HomePageView(TemplateView):
    template_name = "index.html"


## function view
def home_view(request, *args, **kwargs):
    context = {'name': 'Andrii'}
    return render (request, 'home.html', context)

################### *** product detailed view *** ###################
# using python simple function get(pk=pk)
# dynamic id from url + error handling method#1
def product_detailed_view(request, product_id, *args, **kwargs):
    try:
        #obj = Product.objects.get(pk=product_id) ### !!!
        # # ex2: using models: @staticmethod
        obj = Product.get_by_id(product_id)
        # ex3: using all() + filter
        # obj = Product.objects.all().filter(pk=pk)[0]
    except Product.DoesNotExist:
        raise Http404 # this would render html page with HTTP status code
    
    ## optional, when not using template for rendering data (day#2)
    # return HttpResponse(f"Here is a product detailed view of: {obj.id}")
    context = {'object': obj}
    return render (request, 'products/detail.html', context)


# JSON response of product#2 # example just for url
def api_product_detailed_view(request, product_id, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=product_id)
    except Product.DoesNotExist: # 
        raise Http404
        # return JsonResponse({"message": "Not found"}, status=404) # will 
        # return JSON response with HTTP status code of 404
    return JsonResponse({'id': obj.id, 'title': obj.title, 'content': obj.content, 'price': obj.price})


################ *** Product Create View *** #################
# try/except blocks will be excessive as model has it already 
def product_list_view(request, *args, **kwargs):
    products = Product.get_all()
    context = {'product_list': products}

    return render (request, 'products/list_main.html', context)

############################## *** Full List *** ###############################
## getthe list of items in every object
## will get the list of all individual instances of this model
def product_list_view2(request, *args, **kwargs):
    try:
        qs = Product.objects.all()  # list of objects [obj1, obj2, obj3]
    except Product.DoesNotExist:
        raise Http404
    
    ## optional, when not using template for rendering data (day#2)
    # return HttpResponse(f"Here is a product detailed view of: {obj.id}")
    context = {'object_list': qs}
    return render (request, 'products/list.html', context)

## Class-based View as a table
from django.views.generic import ListView

class ProductListView(ListView):
    model = Product
    paginate = 10
    # model.objects.all().order_by('id')
    # class meta in model already ordered the list
    model.objects.all()

################ *** Custom Error Pages *** #################
# def handler404(request,  *args, **kwargs):
#     context = {}
#     response = render(request, '404.html', context)
#     response.status = 404
#     return response


# def handler500(request, *args, **kwargs):
#     context = {}
#     response = render(request, '500.html', context)
#     response.status = 500
#     return response


# def handler400(request, *args, **kwargs):
#     context = {}
#     response = render(request, '400.html', context)
#     response.status = 400
#     return response


# def handler403(request, *args, **kwargs):
#     context = {}
#     response = render(request, '403.html', context)
#     response.status = 403
#     return response


#############################################################


################ *** Methods *** #################

def method_view(request, *args, **kwargs):
    result1 = f'Django request dict: {request.GET} | python standart dict: {dict(request.GET)}'
    result2 = f'Django request dict: {request.POST} | python standart dict: {dict(request.POST)}'
    result3 = request.method == 'GET'
    result4 = request.method == 'POST'
    context = {'result1': result1, 'result2': result2 , 'result3': result3, 'result4': result4}
    return render (request, 'methods.html', context)

#############################################################


################ *** Django Forms *** ################
################ *** Product Create View *** #################

## для можливості виведення повідомлення статусу виконання команди в браузері
from django.contrib import messages
from products.forms import ProductCreationForm


############################## **** Create+Validation Form **** ###############################
def product_create_view(request, *args, **kwargs):
    form = ProductCreationForm(request.POST or None)

    if form.is_valid():
        product = form.save(commit=False)
        
        min_title_length = len(str(form.cleaned_data.get('title'))) > 1
        # print(min_title_length)
        if min_title_length:
            product.save()
            messages.success(request, f'U\'ve just created the next product: {product.title}')
            return redirect ('/products/create/')
        else:
            get_title = form.cleaned_data.get('title')
            messages.error(request, f'{get_title} isn\'t enough long')
            return redirect ('/products/create/')
    
    # fix this later (watch Denis video)
    # else:
    #     messages.error(request, f'make sure U r entering all data in the correct order')

    form = ProductCreationForm()
    context = {'form': form}
    #time.sleep(1.0)
    
#    return render (request, 'forms.html', context) # +
#    return render (request, 'products/create_product_input_tags.html', context) # NOTE: (frontend placeholders)
#     ## !!required fields demand!!
#     # return render (request, 'products/create_product_form_as_p.html', context) # +
    return render (request, 'products/create_product_form_as_crispy_fields.html', context) # NOTE: (backend placeholders)
#    return render (request, 'products/create_product_form_crispy.html', context) # +
############################## **** Update View **** ###############################
def product_update_view(request, product_id,  *args, **kwargs):

    # # context = {'product': product}
    # # return HttpResponse(f'<h2> This is update view {product.title} {product.content} {product.price} </h2>')
    product = Product.get_by_id(product_id)
    form = ProductCreationForm(request.POST or None)

    # reverse form fields to non-required 
    #x = [False for item in form.fields if form.fields[item].required]

    for item in form.fields:
        form.fields[item].required = False if form.fields[item] != 'title' else 0
        
    try:
        for item in form.fields:
            print(form.fields[item].required)
    except Exception as err2:
        print(err2)

    try:
        print(form.is_valid())
        form.save(commit=False)
    except Exception as err3:
        print(err3)

    if form.is_valid():
        #product = form.save(commit=False)
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        price = form.cleaned_data.get('price')
        manufacturers = form.cleaned_data.get('manufacturers')
        print(title, content, price, manufacturers)
        #product.__dict__.update(title=title, content=content, price=price, manufacturers=manufacturers)

        
    context = {'form': form}
    return render (request, 'products/product_update_form_as_crispy_fields.html', context)
    
def product_delete_view(request, product_id, *args, **kwargs):
    product = Product.get_by_id(product_id)
    Product.delete_by_id(product_id)
    messages.success(request, f'U\'ve just deleted the next product: {product.title}') if True else None
    print(messages.__dict__)
    return redirect ('/products/list/')
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

    if request.method == "POST":
        searched = request.POST.get('searched')
        #print(searched)
        # convert user_input to lowercase and split to a single word
        lowercase_and_split = lambda *args: (
            ' '.join(list(map(str, args))).lower().split())

        # # convert db_field to lowercase and split to a single word
        lowercase_and_list = lambda *args: (
            ' '.join([' '.join(i) for i in args]).lower().split())

        # db_fields = Product.get_all() + Manufacturer.get_all()
        # [Product(id=1), Product(id=2), Product(id=3), Product(id=4)]
        
        user_input = lowercase_and_split(searched)
        print(user_input)

        ## 

        all_prod = Product.get_all()
        all_manuf = Manufacturer.get_all()

        ## ['Raspberry Pi', 'Turing Pi', 'PocketBeagle', 'Pine64']
        product_fields = [dict(obj.__dict__).get('title') for obj in all_prod]
        print(product_fields)
        
        ## ['Sony', 'Octavo Systems']
        manufacturer_fields = [dict(obj.__dict__).get('title') for obj in all_manuf]
        print(manufacturer_fields)
        
        # create method id model to cover this
        db_fields = product_fields + manufacturer_fields

        match = [word for word in user_input if word in lowercase_and_list(db_fields)]
        print(match)

        matched_items = list()

        for obj in Product.get_all() + Manufacturer.get_all() :
            for word in match: # match --->  user input
                if word.capitalize() in obj.__dict__.get('title'):
                    matched_items.append(obj)

        matched_items = list(set(matched_items))
        print(matched_items)
        
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
            print('fuck')
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
    print(objects)
    

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

########################################################################################
# # retrieving cleaned data --> Product.objects.create() 
# def product_create_view(request, *args, **kwargs):
    
#     ## if its GET request nothing gonna happen to this form
#     ## so we just put here 'or none'
#     form = ProductCreationForm(request.POST or None) ## --> will avoid if post_data != None: and hard_coding all the staff
#     context = {'form': form}
    
#     if form.is_valid():
#         data = form.cleaned_data
   
#         # standart Django method - create an object I
#         # Product.create(**data) ## will avoid product = Product.create(title=title, content=content, price=price
#         # models classmethod @create - create an object II
#         # **data - means that it'll be keyword args from form: form = {title: 'value', content:'value', price: 'value'}
#         # and etc.
#         product = Product.objects.create(**data)
#         messages.success(request, f"U have just created the next product: {product.title}")
#         # clean up the form while we renew the page
#         form = ProductCreationForm() 
#         if product != None:
#             #messages.success(request, f"U have just created the next product: {product.title}")
#             time.sleep(3)
#             return redirect('/products/list/')
    
    
#     # return render (request, 'forms.html', context) # +
#     # return render (request, 'products/create_product_input_tags.html', context) # +
#     ## !!required fields demand!!
#     # return render (request, 'products/create_product_form_as_p.html', context) # +
#     # return render (request, 'products/create_product_form_as_crispy_fields.html', context) # +
#     return render (request, 'products/create_product_form_crispy.html', context) # +

# ## var2 longer version cleaned data + terminal status check
# def product_create_view(request, *args, **kwargs):
#     context = {}

#     # print(request)
#     # print(request.method)
#     # print(f'{request.POST} is a request method, type is: {type(request.POST)}')
#     # print(dict(request.POST))
#     # print(request.path)

#     # request is a <WSGIRequest: POST '/products/create/'> wrapper that consists of 
#     # metadata about the object, create by HTTP Request, response to a webpage


#     if request.method == 'POST':
#         post_data = request.POST or None
#         if post_data != None:

#             ## instance of a class, that takes request.POST as the atribute (request.POST - > QueryDict)
#             ## form is HTML data
#             form = ProductCreationForm(request.POST)

#             ## check BOOL value, whether all fields in a form correspond to template <input fields> 
#             ## form is a frontend part or HTML structure of the page
#             # print(form)

#             ## BOOL value
#             # print(form.is_valid())

#             ## self cleaned data --> will return clean values from the form
#             ## will get values from cleaned data --> from instance of the class
#             # print(form.cleaned_data)

              ## validated data: means
#             if form.is_valid():
#                 title = form.cleaned_data.get('title')
#                 content = form.cleaned_data.get('content')
#                 price = form.cleaned_data.get('price')

#                 # виведе дані з cleaned_data
#                 print(f'Cleaned data is: {title} | {content} | {price}')

#                 ## will create the object and write it to a database
#                 ## створення через @classmethod моделі
#                 product = Product.create(title=title, content=content, price=price)
#                 # product = Product.objects.create(title=title, content=content, price=price)

#                 ## messages --> виведуть в браузер статус повідомлення
#                 messages.success(request, f"U have just created the next product: {product}")
#                 time.sleep(2)
#                 return redirect('/products/list/')
                  # return HttpResponseRedirect('/products/list/') --> same option of page redirect
                  # 

#     return render (request, 'forms.html', context) # +
#     # return render (request, 'products/create_product_input_tags.html', context) # +
#     # # !!required fields demand!!
#     # return render (request, 'products/create_product_form_as_p.html', context) # +
#     # return render (request, 'products/create_product_form_as_crispy_fields.html', context) # +
#     # return render (request, 'products/create_product_form_crispy.html', context) # +

# # works
# def product_create_view(request, *args, **kwargs):
#     form = ProductCreationForm
#     context = {'form': form}

#     if request.path == '/products/create/':
#         time.sleep(3)
#         return render (request, 'products/create_product.html', context)
#     else:
#         return redirect('/products/list/')

# mine
# def product_create_view(request, product_id=0):

#     if request.method == "GET":
#         if product_id == 0:
#             form = ProductCreationForm()
#         else:
#             product = Product.get_by_id(product_id)
#             form = ProductCreationForm(instance=product)
#             context = {'form': form}
        
#         return render (request, 'products/create_product_input_tags.html', context)

#     elif request.method == "POST":
#         if product_id == 0:
#             form = ProductCreationForm(request.POST)
#         else:
#             product = Product.get_by_id(product_id)
#             form = ProductCreationForm(request.POST, instance=product)
#             # messages.info(request, f'Product is: {product.title}'
#         if form.is_valid():
#             form.save()
#         return redirect('/products/list/') 


# def book_form_view(request, book_id=0):
#     if request.method == 'GET':
#         if book_id == 0:
#             form = BookForm()
#         else:
#             book = Book.get_by_id(book_id)
#             form = BookForm(instance=book)
#         return render(request, 'book/create_book.html', {'form': form})
#     elif request.method == 'POST':
#         if book_id == 0:
#             form = BookForm(request.POST)
#         else:
#             book = Book.get_by_id(book_id)
#             form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#         return redirect('/book/list/')
#############################################################

## dynamic id from url + error handling method#2
# def product_detailed_view(request, id):
#     try:
#         obj = Product.objects.get(id=id)
#         return HttpResponse(f"Here is a product detailed view of: {obj.id}")
#     except ObjectDoesNotExist:
#         raise Http404
#         # return HttpResponse("<h2>This product does not exist</h2>")

# HTTP response of product#1 # example just for url
# def product_detailed_view(request, *args, **kwargs):
#     obj = Product.objects.get(id=1)
#     return HttpResponse(f"Here is product detailed view of: {obj.id}")


