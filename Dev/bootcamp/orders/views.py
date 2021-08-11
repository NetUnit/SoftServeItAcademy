from django.http.response import HttpResponse
from django.shortcuts import render
from orders.models import Order
from products.models import Product
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

# Create your views here.
def order_detailed_view(request, *args, **kwargs):
    pass


def order_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        
        item = request.POST.get('product_order')
        print(item)
        context = {'item': item}
        return HttpResponse('<h2> This is create form </h2>')
        return render (request, 'orders/create_order.html', context)

def cart_view(request, *args, **kwargs):

        if request.method == 'GET':
            request_type = request.method
            product = Product.get_by_id(3)
            order = Order.create(product)
            cart = [item for item in Order.get_all()]
            context = {'cart': cart}
        
            # return HttpResponse(
            #     f'<h2> This is a products_cart. Request method is: {request_type}. \n\
            #     Product: {order.product.title} \n\
            #     Cart: {cart}</h2>'
            #     )
        elif request.method == 'DELETE':
            pass
        #return render (request, 'orders/create_order.html', context={})

        