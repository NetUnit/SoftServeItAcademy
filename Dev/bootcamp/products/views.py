from django.shortcuts import render, redirect

# Create your views here.
from django.http.request import HttpRequest
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product
import time
from django.core.exceptions import ObjectDoesNotExist

# exception handling
from django.template import RequestContext


################# *** Django Generic HomePageView *** #############
from django.views.generic import TemplateView # Import TemplateView

## main page
## Class-based View
class HomePageView(TemplateView):
    template_name = "index.html"


## function view
def home_view(request, *args, **kwargs):
    context = {'name': 'Andrii'}
    return render (request, 'home.html', context)

#####################################################################

# dynamic id from url + error handling method#1
def product_detailed_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404 # this would render html page with HTTP status code
    
    ## optional, when not using template for rendering data (day#2)
    # return HttpResponse(f"Here is a product detailed view of: {obj.id}")
    context = {'object': obj}
    return render (request, 'products/detail.html', context)


# JSON response of product#2 # example just for url
def api_product_detailed_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist: # 
        raise Http404
        # return JsonResponse({"message": "Not found"}, status=404) # will 
        # return JSON response with HTTP status code of 404
    return JsonResponse({'id': obj.id})


## getthe list of items in every object
## will get the list of all individual instances of this model
def product_list_view(request, *args, **kwargs):
    try:
        qs = Product.objects.all()  # list of objects [obj1, obj2, obj3]
    except Product.DoesNotExist:
        raise Http404
    
    ## optional, when not using template for rendering data (day#2)
    # return HttpResponse(f"Here is a product detailed view of: {obj.id}")
    context = {'object_list': qs}
    return render (request, 'products/list.html', context)

# def product_list_view(request, *args, **kwargs):
#     context = {'object_list': Product.get_all}
#     return render(request, 'products/list_2.html', context)


################# *** Custom Error Pages *** #################
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


### remake as product_list_view
# class BookListView(generic.ListView):
#     model = Book
#     paginate = 10
#     model.objects.all().order_by('id')

# class BookDetailView(generic.DetailView):
#     model = Book








