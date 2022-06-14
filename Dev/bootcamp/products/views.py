from django.http import request
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http.request import HttpRequest
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from .models import Product, Manufacturer
import time
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.forms import ValidationError
from django.utils.translation import gettext as _
# exception handling
from django.template import RequestContext

################# *** Django Generic HomePageView *** #############
from django.views.generic import TemplateView, ListView # Import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import SuspiciousFileOperation

###### *** path imports *** ######
import pathlib
from wsgiref.util import FileWrapper
from mimetypes import guess_type
import os

###### *** auth user model *** ########
from django.contrib.auth import get_user_model

###### *** exceptions *** ########
from django.template import RequestContext
# from rest_framework import status

###### *** path imports *** ######
## main page
## Class-based View
class HomePageView(TemplateView):
    template_name = "home.html"

################### *** product detailed view *** ###################
# using python simple function get(pk=pk)
# dynamic id from url + error handling method#1
def product_detailed_view(request, product_id, *args, **kwargs):
    try:
        product = get_object_or_404(Product,  pk=product_id)
        image = product.image

        #obj = Product.get_by_id(product_id) ### !!!
        # # ex2: using models: @staticmethod

        #obj = Product.objects.get(pk=product_id) ### !!!
        # # ex2: using models: @staticmethod

        # ex3: using all() + filter
        # obj = Product.objects.all().filter(pk=product_id)[0]
    except Product.DoesNotExist:
        # this would render html page with HTTP status code
        raise Http404(u'Product wasn\'t found')
    
    ## optional, when not using template for rendering data (day#2)
    # return HttpResponse(f"Here is a product detailed view of: {obj.id}")
    context = {'product': product, 'image': image}
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
    try:
        # print(request.user.is_authenticated)
        products = Product.get_all()
        images = [str(product.image) for product in products]
        #[print(image) for image in images]
        # [print(str(image)) for image in images]
        context = {'product_list': products, 'images': images}
        return render (request, 'products/list_main.html', context)
    except Exception as err:
        print(err)
        pass

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

################ *** Methods *** #################

def method_view(request, *args, **kwargs):
    result1 = f'Django request dict: {request.GET} | python standart dict: {dict(request.GET)}'
    result2 = f'Django request dict: {request.POST} | python standart dict: {dict(request.POST)}'
    result3 = request.method == 'GET'
    result4 = request.method == 'POST'
    context = {'result1': result1, 'result2': result2 , 'result3': result3, 'result4': result4}
    return render (request, 'methods.html', context)

################ *** Product Create View *** #################

## для можливості виведення повідомлення статусу виконання команди в браузері
from django.contrib import messages
from products.forms import ProductCreationForm


############################## **** Create + Validation Form **** ###############################
@staff_member_required(login_url=f'/accounts/check-user-auth/')
def product_create_view(request, *args, **kwargs): ### add user_id here from frontend
    '''
    in this method we r not gonna grab the user_id
    from the url, but instatly take it from the
    request session and write to the db (as a primary key)
    field manufacturers are manually added to the intermediate table
    through models add() method

    '''
    try:
        form = ProductCreationForm(
            request.POST or None,
            request.FILES or None
        )
        
        form.check_manufacturers()
        # print(form.check_manufacturers())
        # print(form.is_valid())
        if form.is_valid():
            form.check_title()
            data = form.cleaned_data
            product = Product.create(**data)
            product.user = request.user

            # image data will be sent through the form
            # no need it's in models
            # image = request.FILES.get('image')
            # product.image = image
            # media = request.FILES.get('media')
            # product.media = media

            # print(product)
            
            product.save()
            messages.success(
                request,
                f'U\'ve just created the next product: {product.title} (^_-)≡☆'
                )
            return redirect ('/products/create/')
        
        messages.error(
                request,
                f'Please make sure to select all fields（♯××）┘ ◎☆')
               
        form = ProductCreationForm()
        context = {'form': form}

    #    return render (request, 'forms.html', context) # +
    #    return render (request, 'products/create_product_input_tags.html', context) # NOTE: (frontend placeholders)
    #     ## !!required fields demand!!
    #     # return render (request, 'products/create_product_form_as_p.html', context) # +
        return render (request, 'products/create_product_form_as_crispy_fields.html', context) # NOTE: (backend placeholders)
    #    return render (request, 'products/create_product_form_crispy.html', context) # +
    except ValidationError as error:
        print(error)
        return render (request, 'form_failure.html', context={'form_error': ''.join(error)})
    except Exception as error1:
        print(error1)
        pass
############################## **** Update View **** ###############################
# def product_update_view(request, product_id,  *args, **kwargs):

#     # # context = {'product': product}
#     # # return HttpResponse(f'<h2> This is update view {product.title} {product.content} {product.price} </h2>')
    
#     product = Product.get_by_id(product_id)
#     form = ProductCreationForm(request.POST or None)
    
#     for item in form.fields:
#         not_title = form.fields[item] != 'title'
#         form.fields[item].required = False if not_title else 0
    
#     if form.is_valid():
#         title = form.cleaned_data.get('title')
#         content = form.cleaned_data.get('content')
#         price = form.cleaned_data.get('price')
#         manufacturers = form.cleaned_data.get('manufacturers')
#         print(title, content, price, manufacturers)
#         product.__dict__.update(
#             title=title,
#             content=content or None,
#             price=price or 0,
#             manufacturers=manufacturers or None)
#         product.save()
#         messages.success(
#             request,
#             f'U\'ve just updated the next product: \'{product.title}\' (ﾉ･_-)☆'
#             )
    
#     context = {'form': form}
#     return render (request, 'products/product_update_form_as_crispy_fields.html', context)

@staff_member_required(login_url=f'/accounts/check-user-auth/')
def product_update_view(request, product_id,  *args, **kwargs):
    try:
        form = ProductCreationForm(
            request.POST or None,
            request.FILES or None
            )
        
        for field in form.fields:
            # make title_not_adjustable 
            # not_title = form.fields[field] != 'title'
            # if not_title:
            form.fields[field].required = False
            


        if form.is_valid():
            data = form.cleaned_data
            product = Product.update_by_id(product_id, data)

            messages.success(request,
                f'U\'ve just updated the next company: \n\
                \'{product.title}\' (ﾉ･_-)☆'
                )

    except Exception as error:
        print(error)
        pass
    
    context = {'form': form}
    return render (
        request, 
        'products/product_update_form_as_crispy_fields.html', 
        context
        )
    
@staff_member_required(login_url=f'/accounts/check-user-auth/')
def product_delete_view(request, product_id, *args, **kwargs):
    product = Product.get_by_id(product_id)
    Product.delete_by_id(product_id)
    messages.success(request, f'\'{product.title}\' has been removed') if True else None
    # print(messages.__dict__)
    return redirect ('/products/list/')

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


######### ****** CORRECT *********** 
# @staff_member_required(login_url=f'/accounts/check-user-auth/')
# def product_create_view(request, *args, **kwargs): ### add user_id here from frontend
### if we want to get user_id we need to grab from url_pattern <user_id>
#     try:
#         form = ProductCreationForm(request.POST or None)
#         form.check_manufacturers()

#         # print(form.is_valid())
#         if form.is_valid():
#             form.check_title()
#             data = form.cleaned_data
#             product = Product.create(**data) ## product = form.save(commit=False)
#             product.save()
            
#             ## write product_id into the db
#             product.user = request.user
#             messages.success(
#                 request,
#                 f'U\'ve just created the next product: {product.title} (^_-)≡☆'
#                 )
#             return redirect ('/products/create/')
        
#         messages.error(
#                 request,
#                 f'Please make sure to select all fields（♯××）┘ ◎☆')
               
#         form = ProductCreationForm()
#         context = {'form': form}
    
#         return render (request, 'products/create_product_form_as_crispy_fields.html', context) # NOTE: (backend placeholders)
#     #    return render (request, 'products/create_product_form_crispy.html', context) # +
#     except ValidationError as error:
#         print(error)
#         return render (request, 'form_failure.html', context={'form_error': ''.join(error)})
#     except Exception as error1:
#         print(error1)
#         pass