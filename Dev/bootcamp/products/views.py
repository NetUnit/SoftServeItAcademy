from django.shortcuts import render, redirect

# Create your views here.
from django.http.request import HttpRequest
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product
import time
from django.core.exceptions import ObjectDoesNotExist


def home_view(request, *args, **kwargs):
    return HttpResponse("<h2>Hello World!</h2>")


# dynamic id from url + error handling method#1
def product_detailed_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404 # this would render html page with HTTP status code
    return HttpResponse(f"Here is a product detailed view of: {obj.id}")


# JSON response of product#2 # example just for url
def api_product_detailed_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist: # 
        return JsonResponse({"message": "Not found"}, status=404) # will 
        # return JSON response with HTTP status code of 404
    return JsonResponse({'id': obj.id})
      

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
