from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

from .models import CustomUser
from accounts.forms import CustomUserCreationForm, LoginForm
from accounts.forms import CustomUserLoginForm, CustomUserUpdateForm
# from accounts.forms import RegisterForm
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from django.contrib import messages
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model

from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy, reverse

from datetime import datetime as dt
from datetime import timedelta as add_minutes

################# *** Panda Hardware *** ###################
def panda_link_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is Panda website: add here info about the website </h2>')

############################## *** Full List *** ########################
def accounts_list_view(request, *args, **kwargs):
    return HttpResponse('<h2> Accounts list should be here </h2>')

################# *** Registration *** ####################
## Function-based View
def register_user_view(request, *args, **kwargs):
    try:
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            data = form.cleaned_data
            # assighn single password
            data['password'] = data.get('password2')
            # del password1/password2 pairs
            [data.pop(f'password{i}') for i in range(1, 3)]
            user = CustomUser()
            # encrypted password will be setup autmatically via model
            new_user = user.create_user(data)
            messages.success(
                request,
                f'U\'ve just created the next user: {new_user.nickname} (^_-)≡☆'
                )
            return redirect ('/accounts/register/')

        form = CustomUserCreationForm()
        context = {'form': form}
        return render (request, 'accounts/register_user_form_as_crispy_fields.html', context)

    except Exception as err:
        print(err)
        pass

## Class-based View
from django.views.generic import CreateView
class RegisterView(CreateView):
    form_class =  CustomUserCreationForm
    template_name = 'accounts/register_user_form_as_crispy_fields.html'
    success_url = '/accounts/login/'
    # success_url = reverse_lazy('/products/list/')

####################### *** Auth *** #######################
## Class-based View
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login_form_as_p.html'

class LoginCounter:

    login_attempt = 0;
    leftover = dt.now(tz=None);

    def __init__(self, login_attempt=login_attempt):
        LoginCounter.login_attempt += 1
        self.login_attempt = LoginCounter.login_attempt

    def count_attempt(self, attempt=None):
        max_attempts = self.login_attempt > 3
        if max_attempts:
            LoginCounter.login_attempt = 0
            self.login_attempt = 0
            return 'This is exception'
        else:
            return self.login_attempt

    def out_of_attempts(self):
        LoginCounter.leftover += add_minutes(minutes=5)
        return self.leftover
        # return LoginCounter.leftover ## same

## Function-based View
def login_user_view(request, *args, **kwargs):
    # print(request.GET)
    elapsed_time = LoginCounter.leftover < dt.now()
    if not elapsed_time and request.method == 'GET':
        return redirect ('/accounts/login-failed/')

    try:
        form = CustomUserLoginForm(request.POST or None)
        if form.is_valid():
        
            email_username = form.cleaned_data.get('email_username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email_username, password=password)

            if user == None:
                attempt = request.session.get('attempt') or 0
                login_attempt = LoginCounter(attempt)
                return redirect('/accounts/login-failed/')

            login(request, user)
            messages.success(
                request,
                f'U\'ve just successfully logined (^_-)≡☆'
                )
            return redirect('/accounts/login-success/')

        form = CustomUserLoginForm()
        context = {'form': form}

        return render (request, 'accounts/login_form_as_p.html', context)

    except Exception as err:
        print(err)
        pass

################# *** Login/Logout Views HTMLS*** ################### +++
def logout_success_view(request, *args, **kwargs):
    logout(request)
    context = {}
    messages.success(request, f'U\'ve been successfully logged out (　ﾟ)(　　)')
    return render(request, 'accounts/logout_success.html', context)

def login_success_view(request, *args, **kwargs):
    messages.success(request, f'U\'ve been successfully logged in (・_・)ノ')
    return render(request, 'accounts/login_success.html', context={})

def login_failed_view(request, *args, **kwargs):
    try:
        attempts = 3 - LoginCounter.login_attempt
        leftover = LoginCounter.leftover
        context = {'attempts': attempts}
        # conditions of elapsed time login trial & 3 attempts
        elapsed_time = leftover < dt.now()
        attempts_left = attempts > 0

        if not elapsed_time:
            leftover = leftover.strftime('%d.%m.%Y %H:%M:%S')
            return render(request, 'accounts/login_failed.html', context={'leftover': leftover})

        if attempts_left and elapsed_time:
            messages.error(request, f'Seem\'s like that username or email was wrong (⇀‸↼‶)')
            return render(request, 'accounts/login_failed.html', context)

        if not attempts_left and elapsed_time:
            out_of_attempts = LoginCounter()
            leftover = out_of_attempts.out_of_attempts().strftime('%d.%m.%Y %H:%M:%S')
            messages.error(request, f'U\'re out of attempts ヾ( ￣O￣)ツ')
            return render(request, 'accounts/login_failed.html', context={'leftover': leftover})
    except Exception as err:
        print(err)
        pass

####################### *** Profile *** #######################
def profile_user_view(request, *args, **kwargs):
    user = request.user
    auth = request.user.is_authenticated
    context = {'user': user, 'auth': auth}
    return render (request, 'accounts/profile_view.html', context)

####################### *** Update User*** #######################
## form isn't valid ### ------
def profile_update_view(request, user_id, *args, **kwargs):
    try:
        form = CustomUserUpdateForm(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            data = form.cleaned_data

            # get user old password
            db_password = CustomUser.get_user_by_id(user_id).password
            print(db_password)

            input_password = data.get('new_password')
            print(input_password)
            #db_password = user.password
            #input_password = data.get('password')
            #print(db_password==input_password)


            #user = CustomUser.get_user_by_id(user_id)
            #print(user)
            #updated_user = CustomUser.update_user_by_id(user_id, data)
            return HttpResponse(f'<h2> This is updated user with {data} | {db_password} {input_password} </h2>')

            
            # messages.success(
            #     request,
            #     f'U\'ve just updated profile with: {username}, password: {email} (^_-)≡☆'
            # )

            # return redirect ('/accounts/profile/')


        form = CustomUserUpdateForm()
        context = {'form': form}
        return render (request, 'accounts/update_user_form_as_crispy_fields.html', context)

    except Exception as err:
        print(err)
        pass

## cbv edit Profile
from django.views.generic import UpdateView
class  EditProfilePageView(generic.UpdateView):
    model = get_user_model()
    template_name = 'accounts/edit_profile_page_CBW.html'
    success_url = '/accounts/login/'
    fields = ('email', 'username', 'password', 'first_name', 'last_name')
    
####################### *** Delete User *** #######################
def profile_delete_view(request, user_id, *args, **kwargs):
    user = get_object_or_404(CustomUser, pk=user_id)
    context = {'user': user}
    return render (request, 'accounts/delete_inquiry.html', context)

import time
def profile_delete_submit(request, user_id, *args, **kwargs):
    CustomUser.delete_user_by_id(user_id)
    time.sleep(1.5)
    return redirect ('/')

################# *** Contact *** ###################
### Put your resume here ###
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is DEV contact: NetUnit -> (095) 013 18 25 </h2>')

#### checker
def show_info(request):
    user = request.user
    try:
        instance = auth_views.LoginView
        #print(instance.get_success_url(instance))
        # x = instance()
        # y = x.get_success_url(request)
        # print(y)
        return HttpResponse(f'<h2> {instance.__dict__} <h2>')
    except Exception as err:
        print(err)
