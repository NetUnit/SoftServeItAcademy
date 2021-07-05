from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

from .models import Accounts

############################## *** Full List *** ########################
def accounts_list_view(request, *args, **kwargs):
    return HttpResponse('<h2> Accounts list should be here  </h2>')


################# *** Registration *** ####################
## custom view
# def register_page(request, *args, **kwargs):
#     return render (request, 'accounts/register.html')


### will use this on the lesson#5 authentication

## Class-based View
from django.views.generic import CreateView

# class RegisterView(CreateView):
#     form_class = RegisterForm                        ### add Register Form
#     template_name = 'authentication/register.html'
#     success_url = '/login/'

## make the same function view

#############################################################


################# *** Authentication *** ####################
## custom view
# def login_page(request, *args, **kwargs):
#     return render (request, 'accounts/login.html')


#############################################################