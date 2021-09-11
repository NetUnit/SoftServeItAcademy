from django import forms
from .models import Order

# bad form import - build a template from here 

from django.utils.html import format_html
from paypal.standard.forms import PayPalPaymentsForm


class CustomPayPalPaymentsForm(PayPalPaymentsForm):
    def render(self):
        return format_html(u"""<form action="{0}" method="post">{1} \n\
            <input type="image" src="{2}" \n\
            border="0" name="submit" alt="Buy it Now" /> </form>""",
            self.get_endpoint(), self.as_p(), self.get_image())


        