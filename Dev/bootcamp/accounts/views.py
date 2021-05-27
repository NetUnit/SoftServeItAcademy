from django.shortcuts import render


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