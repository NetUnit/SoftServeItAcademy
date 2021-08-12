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
            products = [order.product.title for order in Order.get_all()]
            price = sum([order.product.price for order in Order.get_all()])
            orders = [order for order in Order.get_all()]
            zipped = dict(zip(products, orders))

            basket = {}
            for i in range(len(zipped)):
                basket[list(zipped.values())[i]] = []


            try:
                iteration = i <= len(basket) - 1
                for i in range(len(products)):
                    for product in products if iteration else 0:
                        similar_product = product == list(basket.keys())[i].product.title
                        list(basket.values())[i].append(product) if similar_product else 0

            except (IndexError, ValueError, TypeError):
                pass

            print(basket)

            products_amount = 0
            for order, products in basket.items():
                basket[order] = len(products)
                products_amount += len(products)
            
            # add total amount of price
            print(basket, products_amount)
            print(price)
            

            # # correct
            # items = dict([])
            # for i in range(len(orders)):
            #     items[orders[i]] = []

            #print(dict(items))
            
            # dict2 = {}
            # dict2.update(items)
            # print(dict2)

            # filtered_orders = []
            # filtered_orders.append(orders[0])
            # print(filtered_orders)
            # [Order(id=263), Order(id=264), Order(id=265), Order(id=266), Order(id=267), Order(id=268), Order(id=269), Order(id=270)]
            # ['PocketBeagle', 'PocketBeagle', 'Raspberry Pi', 'Raspberry Pi', 'Turing Pi', 'Turing Pi', 'Pine64', 'Pine64']
            # try:
            #     i = 0
            #     for order in orders:
                    
            #         print(filtered_orders[i].product.title)
            #         print(orders[i+1].product.title)

            #         if filtered_orders[i].product.title == orders[i+1].product.title:
            #             print('match')
            #             continue

            #         if filtered_orders[i].product.title != orders[i+1].product.title:
            #             filtered_orders.append(order)
            #             print('append')

            #         i += 1

            #         if i == len(orders):
            #             break
            
            #     print(filtered_orders)

            # except (ValueError, IndexError, TypeError)as err:
            #     print(err)


            # for i in range(len(orders)):
            #     print(i)
            #     print(products[i])
            #     items[orders[i]].append(products[i])
            # print(items)


            # print(zipped)
            # zipped = dict(zipped)
            # print(zipped)


            #print(products)
            #cart = set(cart)
            #print(orders)
            ## зробити тут set 
            ## вирахувати кількість однакових об'єктів + створити context numbers
            ## total 
            ## discount

            context = {'cart': orders}
            #print(context)
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