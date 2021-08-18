from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from orders.models import Order
from products.models import Product
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

# Create your views here.
def order_create_view(request, product_id, *args, **kwargs):
        
    product = Product.get_by_id(product_id)
    order = Order.create(product)
    order.save()
    return redirect ('/order/cart/')


def order_remove_view(request, product_id, *args, **kwargs):
    pass

def cart_clean_view(request, product_id, user_id, *args, **kwargs):
    condition = user_id is not None
    deleted = Order.delete_all()
    return deleted if condition else 0

def cart_view(request, *args, **kwargs):

        # переробити на request.method - POST - створення ордеру
        if request.method == 'GET':
            request_type = request.method
            print(request_type) ## 'GET'
            print(request.path)

            ## get all products title in Order
            products = [order.product.title for order in Order.get_all()]
            
            ## get all order in Order
            orders = [order for order in Order.get_all()]
            zipped = dict(zip(products, orders))

            ## empty basket
            basket = {}
            for i in range(len(zipped)):
                basket[list(zipped.values())[i]] = []

            #print(basket) ## +++ context1

            ## fill the basket
            try:
                iteration = i <= len(basket) - 1
                for i in range(len(products)):
                    for product in products if iteration else 0:
                        similar_product = product == list(basket.keys())[i].product.title
                        list(basket.values())[i].append(product) if similar_product else 0

            except (IndexError, ValueError, TypeError):
                pass
                
            #print(basket)
            
            # lust or product in basket  (not necessarily as we iterate dict in template)
            # items = [i.product.title for i in list(basket.keys())] ## +++ context1
            # print(items)

            products_amount = 0
            for order, products in basket.items():
                basket[order] = len(products)
                products_amount += len(products)

            #print(products_amount) ## +++ context2 quantity

            ## +++ context3 total_value_price
            total_value = float(sum([
                order.product.price for order in Order.get_all()
                ]))
            
            ## discount calculate: 1) disc_ratio discount +++ context4 2) discounted price +++ context5
            ##  - write tests on this part
            #products_amount=50 # in order to check correct
            disc_ratio = ((products_amount//5)*5)/100
            max_disc = int(disc_ratio*100) not in range(0, 50)

            #print(max_disc) ## bool true
            disc_ratio = disc_ratio if not max_disc else 0.5
            #print(disc_ratio)

            discount = int(disc_ratio * 100)
            #print(discount)

            discounted = total_value - total_value * disc_ratio
            #print(discounted)


            context = {'basket': basket,
                'products_amount': products_amount,
                'total_value': total_value,
                'discount': discount,
                'discounted': discounted
            }
            
            return render (request, 'orders/cart.html', context)

            # return HttpResponse(
            #     f'<h2> This is a products_cart. Request method is: {request_type}. Data: {context}. {basket} <h2>'
            #     )




# def product_detailed_view(request, product_id, *args, **kwargs):
#     try:
#         obj = Product.objects.get(pk=product_id) ### !!!
#         # # ex2: using models: @staticmethod
#         # obj = Product.get_by_id(pk)
#         # ex3: using all() + filter
#         # obj = Product.objects.all().filter(pk=pk)[0]
#     except Product.DoesNotExist:
#         raise Http404 # this would render html page with HTTP status code
    
    ## optional, when not using template for rendering data (day#2)
    # return HttpResponse(f"Here is a product detailed view of: {obj.id}")
    # context = {'object': obj}
    # return render (request, 'products/detail.html', context)



# if request.path == '/order/cart/':
#     return redirect ('/order/cart/')
# elif request.path == '/products/list/':
#     return redirect ('/products/list/')
    

    

# bootstrap for pictures
# https://www.quackit.com/bootstrap/bootstrap_5/tutorial/bootstrap_cards.cfm#:~:text=By%20default%2C%20the.card-body%20class%20has%20padding.%20This%20provides,up%20flush%20against%20the%20sides%20of%20the%20card.


            

        ## view cart: some unused logic
            # print(basket)
        
            
            # print(products_amount)
            # print(price)
            

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