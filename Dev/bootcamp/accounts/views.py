from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

from .models import Accounts

################# *** Panda Hardware *** ###################
def panda_link_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is Panda website: add here info about the website </h2>')


############################## *** Full List *** ########################
def accounts_list_view(request, *args, **kwargs):
    return HttpResponse('<h2> Accounts list should be here  </h2>')


################# *** Registration *** ####################
def register_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is a registartion page </h2>')
#     return render (request, 'accounts/register.html')

### will use this on the lesson#5 authentication

## Class-based View
from django.views.generic import CreateView

# class RegisterView(CreateView):
#     form_class = RegisterForm                        ### add Register Form
#     template_name = 'authentication/register.html'
#     success_url = '/login/'

## make the same function view
#####################################################################


################# *** Authentication (Login) *** ####################
def login_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is login </h2>')
#     return render (request, 'accounts/login.html')


################# *** Contact *** ###################
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is DEV contact: NetUnit -> (095) 013 18 25 </h2>')