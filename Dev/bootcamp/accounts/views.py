from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

from .models import CustomUser
from accounts.forms import CustomUserCreationForm, LoginForm
from accounts.forms import CustomUserLoginForm
# from accounts.forms import RegisterForm
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from django.contrib import messages
from django.contrib.auth import get_user_model


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy, reverse


################# *** Panda Hardware *** ###################
def panda_link_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is Panda website: add here info about the website </h2>')


############################## *** Full List *** ########################
def accounts_list_view(request, *args, **kwargs):
    return HttpResponse('<h2> Accounts list should be here </h2>')


################# *** Registration *** ####################
def register_user_view(request, *args, **kwargs):
    try:
        form = CustomUserCreationForm(request.POST or None)
        print(form.is_valid())

        if form.is_valid():
            user = form.save(commit=False)

            # get the data here
            data = form.cleaned_data
            # assighn single password
            data['password'] = data.get('password2')
            # del password1/password2 pairs
            [data.pop(f'password{i}') for i in range(1, 3)]
            #print(data)

            user = CustomUser()
            new_user = user.create_user(data)
            #print(new_user)
            # update db data - Custom.user(update)

            messages.success(
                request,
                f'U\'ve just created the next user: {data} (^_-)≡☆'
                )
            return redirect ('/accounts/register/')

        form = CustomUserCreationForm()
        context = {'form': form}
        return render (request, 'accounts/register.html', context)
    # return render (request, 'accounts/create_user_form_as_crispy_fields.html', context)

    except Exception as err:
        print(err)
        pass
## will use this on the lesson#5 authentication

## Class-based View
from django.views.generic import CreateView
class RegisterView(CreateView):
    form_class =  CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/products/list/'
    # success_url = reverse_lazy('/products/list/')

#########################################################
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login_form_as_p.html'


def login_user_view(request, *args, **kwargs):
    try:
        form = CustomUserLoginForm(request.POST or None)
        print(form.is_valid())

        if form.is_valid():
            user = form.cleaned_data
            print(user)

            # update db data - Custom.user(update)

            user = form.save(commit=False)
            messages.success(
                request,
                f'U\'ve just logined with the next username {user}(^_-)≡☆'
                )
            return redirect ('/products/list/')
        
        form = CustomUserLoginForm()
        context = {'form': form}

    #    return HttpResponse('<h2> This is login </h2>')
        return render (request, 'accounts/login_form_as_crispy_tags.html', context)
    #    return render (request, 'accounts/login_user_form_as_crispy_fields.html', context)

    except Exception as err:
        print(err)
        pass

################# *** Authentication (Login) *** ####################
# def login_user_view(request, *args, **kwargs):
#     try:
#         form = CustomUserLoginForm(request.POST or None)
#         print(form)

#         if form.is_valid():
#             print(form.is_valid())

#             user = form.cleaned_data
#             print(user)

#             # update db data - Custom.user(update)

#             user = form.save(commit=False)
#             messages.success(
#                 request,
#                 f'U\'ve just logined with the next username {user}(^_-)≡☆'
#                 )
#             return redirect ('/products/list/')
        
#         form = CustomUserLoginForm()
#         context = {'form': form}

#     #    return HttpResponse('<h2> This is login </h2>')
#         return render (request, 'accounts/login.html', context)
#     #    return render (request, 'accounts/login_user_form_as_crispy_fields.html', context)

#     except Exception as err:
#         print(err)
#         pass


################# *** Contact *** ###################
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is DEV contact: NetUnit -> (095) 013 18 25 </h2>')