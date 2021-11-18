from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.http import  JsonResponse

# from orders.models import Order
from .models import Product, Order
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView

# payment
from django.conf import settings
from decimal import Decimal
from django.views.generic import FormView

# https://www.gravityforms.com/pricing/ - 59 usd
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
import datetime
from datetime import date
from time import strftime

# Create your views here

# @login_required(login_url=f'/accounts/check-user-auth/')
def order_create_view(request, product_id, *args, **kwargs):
    try:
        product = Product.get_by_id(product_id)
        order = Order.create(product) if product else None
        #print(isinstance(request.user, AnonymousUser))
        # in the case not user.is_authenticated()
        if isinstance(request.user, AnonymousUser):
            order.user = None
            # print(order.user)
            return redirect('/order/cart/')

        order.user = request.user
        order.save()

        # print(order.user)
        # print(request.user)
        # order.save
        # return HttpResponse (
        #     f'<h3>  {order}  <h3>'
        # )
        return redirect('/order/cart/')

    except Exception as error:
        print(error)

# @login_required(login_url=f'/accounts/check-user-auth/')
def order_remove_view(request, order_id, *args, **kwargs):
    Order.delete_by_id(order_id)
    return redirect('/order/cart/')

    # return HttpResponse (
    #     f'<h3>  {order_id} {Order.delete_by_id(order_id)}  <h3>'
    # )

# @login_required(login_url=f'/accounts/check-user-auth/')
def cart_clean_view(request, *args, **kwargs):  # add these later: product_id, user_id,
    try:
        #condition = user_id is not None
        user = request.user
        user_id = user.id
        # print(user_id)

        Order.delete_all(user_id)

       #order = Order.objects.all().filter(user_id=user_id)
        # print(order)

        # print(Order.delete_all(user_id))

        messages.success(request, f'Your cart is empty now (-ˍ-。)')
        return redirect('/order/cart/')
    except Exception as error:
        print(error)


def cart_view(request, *args, **kwargs):

    user = request.user
    user_id = user.id

    # context#1
    basket = Order.cart_items_amount(user_id)
    # [print(order.product.manufacturers) for order in list(basket.keys())]

    # context#2
    products_amount = Order.products_amount(user_id)

    # context#3 total_value_price
    total_value = Order.total_value(user_id)

    # context#4 discount
    disc_ratio = Order.get_discount(user_id)
    discount = int(disc_ratio * 100)

    # context#5 price after discount
    discounted = total_value - total_value * disc_ratio

    context = {'basket': basket,
               'products_amount': products_amount,
               'total_value': total_value,
               'discount': discount,
               'discounted': discounted
               }

    return render(request, 'orders/cart.html', context)


@login_required(login_url=f'/accounts/check-user-auth/')
def process_payment_view(request, *args, **kwargs):
    try:
        instance = Order()
        form = PayPalPaymentsForm()
        
        user = request.user
        user_id = user.id
        
        order_id = max(
            [order.id for order in Order.get_orders_by_user(user.id)]
        )
        
        to_decimal = lambda value: Decimal(str(value))

        total_value = Order.total_value(user_id)
        total_value = to_decimal(total_value)

        order = Order.get_orders_by_user(user_id)
        host = request.get_host() 

        basket = Order.cart_items_amount(user_id)

        invoice_basket  = instance.get_value_per_amount(user_id)
        shipping = 20
        shipping = to_decimal(shipping)
        
        date = datetime.date.today()
        
        # check amounts
        #[print(item.amounts) for item in list(invoice_basket.keys())]
        # 'amount': '%.2f' % order.get_total_value().quantize(Decimal('1.000'))

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'personal': user.email,
            'shipping': '%.2f' % shipping.quantize(Decimal('1.000')),
            'amount': '%.2f' % total_value.quantize(Decimal('1.000')),
            'total_cart_amount': '%.2f' % (20 + total_value).quantize(Decimal('1.000')),
            'basket': Order.cart_items_amount(user_id),
            'invoice_basket': invoice_basket,
            'user': user,
            'item_name': f'Order: {order_id}',
            'invoice': str(order_id),
            'currency_code': 'USD',
            'date': date,
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": request.build_absolute_uri(reverse('orders:paypal-return')),
            "cancel_return": request.build_absolute_uri(reverse('orders:paypal-cancel')),
            # 'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            # 'cancel_return': 'http://{}{}'.format(host, reverse('orders:paypal-cancel')),
        }

        form = PayPalPaymentsForm(initial=paypal_dict)
        context = {'form': form, 'order': order, 'data': paypal_dict}
        return render(request, 'orders/paypal_invoice.html', context)

    except Exception as err:
        print(err)
        pass

## method#2
class PaypalFormView(FormView):
    template_name = 'orders/paypal_form2.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
        user = self.request.user
        order_id = max(
            [order.id for order in Order.get_orders_by_user(user.id)]
        )
        try:

            paypal_dict = {
                "business": 'myXbox@bigmir.net',
                "amount": Order.total_value(user.id),
                "currency_code": "USD",
                "item_name": f'Order {order_id}',
                "invoice": str(order_id),
                "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
                "return_url": self.request.build_absolute_uri(reverse('orders:paypal-return')),
                "cancel_return": self.request.build_absolute_uri(reverse('orders:paypal-cancel')),
                "lc": 'EN',
                "no_shipping": '1',
            }

            return paypal_dict

        except Exception as err:
            print(err)
            pass


def payment_complete_view(request):
    try:
        body = json.loads(request.body)
        print(body)
        order = Order.objects.get(id=body['orderId'])
        return JsonResponse('Payment Completed', safe=False)

    except Exception as err:
        print(err)
        pass


class PaypalReturnView(TemplateView):
    template_name = 'orders/payment_done.html'


class PaypalCancelView(TemplateView):
    template_name = 'orders/payment_cancelled.html'


#################### *** API PAYPAL RETURN *** ####################
def api_process_payment_view(request, *args, **kwargs):

    '''
        returns a JSON data that 
        contains all payment attributes,
        for further processing via test.js
        script

    '''
    try:
        form = PayPalPaymentsForm()
        user = request.user
        user_id = user.id
        order_id = user_id

        total_value = Order.total_value(user_id)
        total_value = Decimal(str(total_value))

        order = Order.get_orders_by_user(user_id)
        host = request.get_host()

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'personal': user.email,
            'amount': '%.2f' % total_value.quantize(Decimal('1.000')),
            'item_name': f'Order: {order_id}',
            'invoice': str(order_id),
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'cancel_return': 'http://{}{}'.format(host, reverse('orders:paypal-cancel')),
        }

        json_data = JsonResponse(paypal_dict)
        
        #json_data = json.dumps(paypal_dict)
        #return JsonResponse(json_data, safe=False)

        form = PayPalPaymentsForm(initial=paypal_dict)
        context = {'form': form, 'order': order, 'data': json_data}
        return render(request, 'orders/test_js/employees.html', context)

    except Exception as err:
        print(err)
        pass

#################### *** API PAYPAL RETURN *** ####################

# order cart view - WHOLE
# def cart_view(request, *args, **kwargs):

#         # переробити на request.method - POST - створення ордеру
#         if request.method == 'GET':
#             request_type = request.method
#             #print(request_type) ## 'GET'
#             #print(request.path)

#             ## get all products title in Order
#             products = [order.product.title for order in Order.get_all()]
#             ## print(products) ++

#             ## get all order in Order
#             orders = [order for order in Order.get_all()]
#             print(orders)
#             zipped = dict(zip(products, orders))

#             ## form empty basket: key - order, value - list of products
#             basket = {}
#             for i in range(len(zipped)):
#                 basket[list(zipped.values())[i]] = []

#             print(basket) ## +++ context1

#             try:
#                 for i in range(len(products)):
#                     iteration = i <= len(basket) - 1
#                     print(iteration)
#                     for product in products if iteration else 0:
#                         similar_product = product == list(basket.keys())[i].product.title
#                         list(basket.values())[i].append(product) if similar_product else 0
#             except TypeError as err:
#                 print(err)


#             # print(basket)

#             # lust or product in basket  (not necessarily as we iterate dict in template)
#             # items = [i.product.title for i in list(basket.keys())] ## +++ context1
#             # print(items)

#             products_amount = 0
#             for order, products in basket.items():
#                 basket[order] = len(products)
#                 products_amount += len(products)

#             #print(products_amount) ## +++ context2 quantity

#             ## +++ context3 total_value_price
#             total_value = float(sum([
#                 order.product.price for order in Order.get_all()
#                 ]))

#             #print(total_value)
#             ## discount calculate: 1) disc_ratio discount +++ context4 2) discounted price +++ context5
#             ##  - write tests on this part
#             #products_amount=50 # in order to check correct
#             disc_ratio = ((products_amount//5)*5)/100
#             max_disc = int(disc_ratio*100) not in range(0, 50)

#             #print(max_disc) ## bool true
#             disc_ratio = disc_ratio if not max_disc else 0.5
#             #print(disc_ratio)

#             ## +++ context4 discount
#             discount = int(disc_ratio * 100)
#             #print(discount)

#             ## +++ context5 discounted
#             discounted = total_value - total_value * disc_ratio
#             #print(discounted)


#             context = {'basket': basket,
#                 'products_amount': products_amount,
#                 'total_value': total_value,
#                 'discount': discount,
#                 'discounted': discounted
#             }

#             return render (request, 'orders/cart.html', context)

#             # return HttpResponse(
#             #     f'<h2> This is a products_cart. Request method is: {request_type}. Data: {context}. {basket} <h2>'
#             #     )


# def product_detailed_view(request, product_id, *args, **kwargs):
#     try:
#         obj = Product.objects.get(pk=product_id) ### !!!
#         # # ex2: using models: @staticmethod
#         # obj = Product.get_by_id(pk)
#         # ex3: using all() + filter
#         # obj = Product.objects.all().filter(pk=pk)[0]
#     except Product.DoesNotExist:
#         raise Http404 # this would render html page with HTTP status code

    # optional, when not using template for rendering data (day#2)
    # return HttpResponse(f"Here is a product detailed view of: {obj.id}")
    # context = {'object': obj}
    # return render (request, 'products/detail.html', context)


# if request.path == '/order/cart/':
#     return redirect ('/order/cart/')
# elif request.path == '/products/list/':
#     return redirect ('/products/list/')


# bootstrap for pictures
# https://www.quackit.com/bootstrap/bootstrap_5/tutorial/bootstrap_cards.cfm#:~:text=By%20default%2C%20the.card-body%20class%20has%20padding.%20This%20provides,up%20flush%20against%20the%20sides%20of%20the%20card.

    # view cart: some unused logic
    # print(basket)

    # print(products_amount)
    # print(price)

    # # correct
    # items = dict([])
    # for i in range(len(orders)):
    #     items[orders[i]] = []

    # print(dict(items))

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

    # print(products)
    #cart = set(cart)
    # print(orders)class PaypalFormView(FormView):
#     template_name = 'orders/paypal_form.html'
#     form_class = PayPalPaymentsForm

#     def get_initial(self):
#         return {
#             "business": 'andriyproniyk@gmail.com',
#             "amount": 20, # Order.get_amount()
#             "currency_code": "EUR",
#             "item_name": 'Example item',
#             "invoice": 1234,
#             "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
#             "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
#             "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
#             "lc": 'EN',
#             "no_shipping": '1',
#         }
