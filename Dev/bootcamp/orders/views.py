from django.http.response import HttpResponse
from django.shortcuts import render
from orders.models import Order
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

# Create your views here.
def order_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        
        item = request.POST.get('product_order')
        print(item)
        context = {'item': item}
        return HttpResponse('<h2> This is create form </h2>')
        return render (request, 'orders/create_order.html', context)

def cart_view(request, *args, **kwargs):
        return HttpResponse('<h2> This is a products_cart </h2>')