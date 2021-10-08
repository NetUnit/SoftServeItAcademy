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
        return render (request, 'accounts/register_user_form_as_crispy_fields.html', context)

    except Exception as err:
        print(err)
        pass
## will use this on the lesson#5 authentication

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

## Function-based View
def login_user_view(request, *args, **kwargs):
    try:
        form = CustomUserLoginForm(request.POST or None)
        print('Form is valid') if form.is_valid() else 'Form is NOT valid'

        if form.is_valid():
            user = form.cleaned_data

            email = user.get('username')
            password = user.get('password')

            # user.set_password('password') ## !!! password should be encrypted
            
            user = authenticate(request, username=email, password=password) ## None
            print(request.user.is_authenticated)

            messages.success(
                request,
                f'U\'ve just logined with the next email: {email}, password: {password} (^_-)≡☆'
                )
            return redirect ('/accounts/login/')
        
        form = CustomUserLoginForm()
        context = {'form': form}

    #    return HttpResponse('<h2> This is login </h2>')
        return render (request, 'accounts/login_user_form_as_crispy_fields.html', context)
    #    return render (request, 'accounts/login_form_as_p.html', context)

    except Exception as err:
        print(err)
        pass

################# *** Contact *** ################### +++
def logout_view(request, *args, **kwargs):
    logout(request)
    context = {}
    messages.success(request, f'U\'ve been successfully logged out')
    return render(request, 'accounts/logout.html', context)

####################### *** Profile *** #######################

def profile_user_view(request, *args, **kwargs):
    user = request.user
    auth = request.user.is_authenticated
    
    context = {'user': user, 'auth': auth}

    # return render (request, 'accounts/profile.html', context)
    return render (request, 'accounts/user_detail.html', context)
    # return HttpResponse(f'<h2> {user}, user is_authenticated: {auth} <h2>')

####################### *** Update User*** #######################
## form isn't valid
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

## CBW edit Profile
from django.views.generic import UpdateView
class  EditProfilePageView(generic.UpdateView):
    model = get_user_model()
    template_name = 'accounts/edit_profile_page_CBW.html'
    success_url = '/accounts/login/'
    fields = ('email', 'username', 'password', 'first_name', 'last_name')

def set_password(request, *args, **kwargs):
    user = request.user
    auth = request.user.is_authenticated
    password = 'Passw0rd20022016_'

    #user.set_password(password)

    context = {'user': user, 'auth': auth, 'password': password}
    return HttpResponse(f'<h2> {context} <h2>')
    

####################### *** Delete User*** #######################
def profile_delete_view(request, user_id, *args, **kwargs):
    return CustomUser.delete_user_by_id(user_id)

################# *** Contact *** ###################
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is DEV contact: NetUnit -> (095) 013 18 25 </h2>')