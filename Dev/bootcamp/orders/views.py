from django.http.response import HttpResponse
from django.shortcuts import render
from orders.models import Order
from products.models import Product
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

# Create your views here.
def order_detailed_view(request, *args, **kwargs): # order_id,
    pass
    # request_type = request.method
    # # order = Order.objects.get(pk=order_id)
    # order = Order.objects.get(2)
    # return HttpResponse(
    #     f'<h2> This is order detailed view {request_type }. Order is: {order.product.title} </h2>'
    #     )

def order_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        
        item = request.POST.get('product_order')
        print(item)
        context = {'item': item}
        return HttpResponse('<h2> This is create form </h2>')
        return render (request, 'orders/create_order.html', context)

def cart_view(request, *args, **kwargs):

        # переробити на request.method - POST - створення ордеру
        if request.method == 'GET':
            request_type = request.method
            product = Product.get_by_id(3)
            order = Order.create(product)
            cart = [item for item in Order.get_all()]
            print(cart)
            context = {'cart': cart}
            print(context)
            return render (request, 'orders/cart.html', context)

            # return HttpResponse(
            #     f'<h2> This is a products_cart. Request method is: {request_type}. \n\
            #     Product: {order.product.title} \n\
            #     Cart: {cart}</h2>'
            #     )
        # elif request.method == 'DELETE':
        #     pass
        #return render (request, 'orders/create_order.html', context={})

        

# bootstrap for pictures
# https://www.quackit.com/bootstrap/bootstrap_5/tutorial/bootstrap_cards.cfm#:~:text=By%20default%2C%20the.card-body%20class%20has%20padding.%20This%20provides,up%20flush%20against%20the%20sides%20of%20the%20card.