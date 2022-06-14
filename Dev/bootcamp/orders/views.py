from .models import Product, Order, CustomUser
from django.contrib.auth.models import AnonymousUser
from django.http.response import (
    HttpResponse, JsonResponse,
    Http404,
    HttpResponseRedirect
)

from django.urls import (
    reverse_lazy,
    reverse
)

from django.http import (
    HttpResponse, JsonResponse,
    Http404,
    HttpResponseRedirect
)

from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView

# payment
from django.conf import settings
from decimal import Decimal
from django.views.generic import FormView

# https://www.gravityforms.com/pricing/
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
import datetime
from datetime import date
from time import strftime

# path
import pathlib
from wsgiref.util import FileWrapper
from mimetypes import guess_type


# @login_required(login_url=f'/accounts/check-user-auth/')
def order_create_view(request, product_id, *args, **kwargs):

    product = Product.get_by_id(product_id)
    order = Order.create(product) if product else None
    # in case not user.is_authenticated()
    if isinstance(request.user, AnonymousUser):
        order.user = None
        return redirect('/order/cart/user/')

    order.user = request.user
    order.save()
    return redirect(f'/order/cart/user/{order.user.id}')


# @login_required(login_url=f'/accounts/check-user-auth/')
def order_remove_view(request, order_id, *args, **kwargs):
    order = Order.get_by_id(order_id)
    user_id = order.user.id
    Order.delete_by_id(order_id)
    return redirect(f'/order/cart/user/{user_id}')

    # only for test
    # return HttpResponse (
    #     f'<h3>  {order_id} {Order.delete_by_id(order_id)}  <h3>'
    # )


# @login_required(login_url=f'/accounts/check-user-auth/')
def cart_clean_view(request, *args, **kwargs):
    # condition = user_id is not None
    user = request.user
    user_id = user.id
    Order.delete_all(user_id)
    messages.success(request, f'Your cart is empty now (-ˍ-。)')
    return redirect(f'/order/cart/user/{user_id}')


def cart_view(request, user_id=None, *args, **kwargs):
    '''
    context#6 corresponds to get_absolute_url()
    method & shows limited acces from admin session
    to a cart of selected user

    :returns: context value with main key-value
    pairs connected to user's cart data

    .. note::
        limited rights if admin accesses user's cart
        with not_admin_url meant user_id is not
        admin's id. admin cannot remove or change
        cart items.
    '''
    # context #1
    user = request.user
    basket = Order.cart_items_amount(user_id)

    # context #2
    products_amount = Order.products_amount(user_id)
    # print(products_amount)
    # context #3 total_value_price
    total_value = Order.total_value(user_id)
    # print(total_value)
    # context #4 discount
    disc_ratio = Order.get_discount(user_id)
    discount = int(disc_ratio * 100)

    # context #5 price after discount
    discounted = total_value - total_value * disc_ratio

    # context #6 limited access from admin to user's cart
    not_admin_url = user_id == str(request.user.id)

    context = {
        'basket': basket,
        'products_amount': products_amount,
        'total_value': total_value,
        'discount': discount,
        'discounted': discounted,
        'not_admin_url': not_admin_url,
        'user': user
    }

    return render(request, 'orders/cart.html', context)


@login_required(login_url=f'/accounts/check-user-auth/')
def process_payment_view(request, *args, **kwargs):

    instance = Order()
    form = PayPalPaymentsForm()

    user = request.user
    user_id = user.id

    order_id = max(
        [order.id for order in Order.get_orders_by_user(user.id)]
    )

    def to_decimal(value): return Decimal(str(value))

    total_value = Order.total_value(user_id)
    total_value = to_decimal(total_value)

    order = Order.get_orders_by_user(user_id)
    order = order.order_by('-id').first()
    host = request.get_host()

    basket = Order.cart_items_amount(user_id)

    invoice_basket = instance.get_value_per_amount(user_id)
    shipping = 20
    shipping = to_decimal(shipping)

    date = datetime.date.today()

    # check amounts
    # [print(item.amounts) for item in list(invoice_basket.keys())]

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


def order_download_view(request, user_id, *args, **kwargs):
    '''
    Download the order media if such exists
    '''
    qs = Product.objects.all().filter(user_id=user_id)
    product = qs.order_by('-id').first()

    if not product.media:
        raise Http404

    media = product.media
    product_path = media.path

    product_id = product.id

    # path = <class 'pathlib.PosixPath'>
    path = pathlib.Path(product_path)
    if not path.exists():
        raise Http404

    # file extention '.jpg'
    ext = path.suffix
    file_name = f'cool-moto-product-{product_id}{ext}'

    # opens file through a path from pathlib
    # 'rb' read as bites
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


# method #2
class PaypalFormView(FormView):
    template_name = 'orders/paypal_form2.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
        user = self.request.user
        order_id = max(
            [order.id for order in Order.get_orders_by_user(user.id)]
        )

        paypal_dict = {
            "business": 'myXbox@bigmir.net',
            "amount": Order.total_value(
                user.id),
            "currency_code": "USD",
            "item_name": f'Order {order_id}',
            "invoice": str(order_id),
            "notify_url": self.request.build_absolute_uri(
                reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(
                reverse('orders:paypal-return')),
            "cancel_return": self.request.build_absolute_uri(
                reverse('orders:paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1',
        }

        return paypal_dict


def payment_complete_view(request):

    body = json.loads(request.body)
    order = Order.objects.get(id=body['orderId'])
    return JsonResponse('Payment Completed', safe=False)


class PaypalReturnView(TemplateView):
    template_name = 'orders/payment_done.html'


class PaypalCancelView(TemplateView):
    template_name = 'orders/payment_cancelled.html'


# *** API PAYPAL RETURN *** #
def api_process_payment_view(request, *args, **kwargs):
    '''
    returns a JSON data that
    contains all payment attributes,
    for further processing via test.js
    script
    '''
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

    # json_data = json.dumps(paypal_dict)
    # return JsonResponse(json_data, safe=False)

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form, 'order': order, 'data': json_data}
    return render(request, 'orders/test_js/employees.html', context)
