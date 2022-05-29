from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.utils.translation import gettext as _
from django.forms import ValidationError

from .models import CustomUser
from accounts.forms import CustomUserLoginForm, LoginForm
from accounts.forms import  CustomUserCreationForm, CustomUserUpdateForm
# from accounts.forms import RegisterForm
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from django.contrib import messages
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy, reverse

from datetime import datetime as dt
from datetime import timedelta as add_minutes

###### *** path imports *** ######
import pathlib
from wsgiref.util import FileWrapper
from mimetypes import guess_type

##### *** time *** #####
import time
### *** decorators *** ###
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

### *** exceptions *** ###
from accounts.exceptions import CustomAuthFailed

############################## *** Full List *** ########################
def accounts_list_view(request, *args, **kwargs):
    return HttpResponse('<h2> Accounts list should be here </h2>')

################# *** Registration FBV + CBV  *** ####################
## Function-based View
def register_user_view(request, *args, **kwargs):
    try:
        form = CustomUserCreationForm(
            request.POST or None,
            request.FILES or None
            )
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
            if not new_user:
                raise ValidationError(
                    _(f'User hasn\'t been created'),
                    code='invalid'
                    )
            messages.success(
                request,
                f'U\'ve just created the next user: {new_user.username} (^_-)≡☆'
                )
            return redirect ('/accounts/register-fbv/')

        form = CustomUserCreationForm()
        context = {'form': form}
        return render(
            request, 
            'accounts/register_user_form_as_crispy_fields.html', 
            context
            )

    except Exception as err:
        print(err)
        pass


## Class-based View
from django.views.generic import CreateView
class RegisterView(CreateView):
    form_class =  CustomUserCreationForm
    template_name = 'accounts/register_user_form_as_crispy_fields.html'
    success_url = '/accounts/login-fbv/'
    # success_url = reverse_lazy('/products/list/')

####################### *** Auth *** #######################
## Class-based Views
class CustomLoginView(auth_views.LoginView):
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
            raise CustomAuthFailed
        else:
            return self.login_attempt

    def out_of_attempts(self):
        LoginCounter.leftover += add_minutes(minutes=5)
        return self.leftover
        # return LoginCounter.leftover ## same

## Function-based View
def login_user_view(request, *args, **kwargs):
    elapsed_time = LoginCounter.leftover < dt.now()
    if not elapsed_time and request.method == 'GET':
        return redirect('/accounts/login-failed/')

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

#################### *** Login/Logout Views *** ######################
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
            return render(
                request,
                'accounts/login_failed.html',
                context={'leftover': leftover}
                )

        if attempts_left and elapsed_time:
            messages.error(
                request,
                f'Seem\'s like that username or email was wrong (⇀‸↼‶)'
                )
            return render(request, 'accounts/login_failed.html', context)

        if not attempts_left and elapsed_time:
            out_of_attempts = LoginCounter()
            leftover = out_of_attempts.out_of_attempts().strftime('%d.%m.%Y %H:%M:%S')
            messages.error(request, f'U\'re out of attempts ヾ( ￣O￣)ツ')
            return render(request, 'accounts/login_failed.html', context={'leftover': leftover})
    except Exception as err:
        print(err)
        pass

def ban_user_view(request, user_id):
    user = CustomUser.get_user_by_id(user_id)
    return HttpResponse(f'<h2> This is banned user {user_id} <h2>') 

def logout_success_view(request, *args, **kwargs):
    logout(request)
    context = {}
    messages.success(
        request,
        f'U\'ve been successfully logged out (　ﾟ)(　　)'
        )
    return render(request, 'accounts/logout_success.html', context)

####################### *** Profile *** #######################
def profile_user_view(request, user_id=None, *args, **kwargs):
    # print(user_id)
    # print(request.user)
    user_id = None if user_id == 'None' else user_id
    if user_id is None:
        user = request.user
    else:
        user = CustomUser.get_user_by_id(user_id)
    auth = user.is_authenticated
    # print(user, auth)
    context = {'user': user, 'auth': auth}
    return render (request, 'accounts/profile_view.html', context)

@staff_member_required(login_url=f'/accounts/check-user-auth/')
def profile_list_view(request, *args, **kwargs):
    try:
        profiles = CustomUser.get_all_users()
        context = {'profiles': profiles}
        return render(request, 'accounts/list_main.html', context)
        # return HttpResponse(f'<h2> {profiles}  <h2>')
    except ValidationError as error:
        ### change this afterwards to general template
        ### put error as general name of eror in a template for all views
        return render(request, 'accounts/update_faied.html')

####################### *** Update User FBV *** #######################
def update_success_view(request, user_id, *args, **kwargs):
    try:
        user = CustomUser.get_user_by_id(user_id)
        context = {'user': user}
        messages.success(
            request,
            f'User: {user} has been successfully updated ๏[-ิ_•ิ]๏'
            )
        return render(request, 'accounts/update_success.html', context)
    except Exception as err:
        print(err)

def status_update_view(request, user_id, *args):
    try:
        user = CustomUser.get_user_by_id(user_id)
        password = user.password
        user.set_password(password)
        user.save()
        context = {'user': user}
        messages.success(
            request,
            f'User: {user} has been successfully updated ๏[-ิ_•ิ]๏'
            )
        return render(request, 'accounts/update_success.html', context)

    except Exception as err:
        print(err)

def profile_update_view(request, user_id, *args, **kwargs):

    try:
        form = CustomUserUpdateForm(
            request.POST or None,
            request.FILES or None
        )
        if form.is_valid():

            # FORM: check whether the previous password is correct
            form.check_user(request, user_id)

            # FORM: setup a new password & validate
            password = form.clean_password()
            form.password_validation(password)
            
            # get data from the a form
            data = form.cleaned_data

            # prepare new data set to record into db, remove excessive items
            [data.pop(f'password{i}') for i in range(1, 3)]
            data.pop('old_password')

            # update user
            user = CustomUser.update_user_by_id(user_id, data)
            
            # asigh and ecrypt new password
            user.set_password(password)
            delattr(user, '_password')
            user.save()
            
            messages.success(
                request,
                f'U\'ve just updated profile with: {user.email}, password: {user.password} (^_-)≡☆'
            )

            return redirect(f'/accounts/update-success/{user_id}')

        form = CustomUserUpdateForm()
        context = {'form': form}
        return render (request, 'accounts/edit_profile_fbv.html', context)
    
    except ValidationError as psw_error:
        return render (request, 'accounts/update_failed.html', context={'psw_error': ''.join(psw_error)})

    except Exception as err:
        print(err)
        pass

####################### *** Update User CBV *** #######################
from django.views.generic import UpdateView

class  EditProfilePageView(generic.UpdateView, CustomUser): #CustomUserUpdateForm

    '''
        :get_form_kwargs(): returns kwargs of parental class UpdateView
        kwars r form fields that is written to db
        :get_object: returns the object the view is displaying and then
        changing it's fields with ne data get with POST method
    
    '''

    model = get_user_model()
    template_name = 'accounts/edit_profile_cbv.html'
    success_url = '/accounts/update-success/'
    fields = ('email', 'username',
            'password', 'first_name',
            'last_name', 'image', 'media'
        )

    # slug_field = 'slug'
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not hasattr(self, 'object'):
            raise Http404(_('User wasn\'t found, but it\'s not your fault'))

        user_id = self.object.id
        self.success_url = f'/accounts/update-success/{user_id}'

        if self.request.method == "GET":
            kwargs.update({'instance': self.object})
            return kwargs

        if self.request.method == "POST":
            data = kwargs.get('data')
            password = data.get('password')
            
            user = self.request.user
            user.set_password(password)
            
            _mutable = data._mutable
            data._mutable = True

            data['password'] = user.password

            data._mutable = _mutable
            return kwargs


    # def __init__(self, *args, **kwargs):
    #     self.kwargs = None
    #     super().__init__(*args)


    # def get_object(self, queryset=None, *args, **kwargs):
    #     '''
    #         Return the object the view is displaying.
    #         Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
    #         Subclasses can override this to return any object.

    #         self.kwargs: dict() containing main object info {'pk': int}
    #         self.pk_url_kwarg: key corresponds to pk(user) from url
    #         self.get_queryset(): get queryset of all model class related objects
    #     '''
    #     # Use a custom queryset if provided; this is required for subclasses
    #     # like DateDetailView
    #     print(self.kwargs)
    #     print(self.pk_url_kwarg)
            
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #         print(queryset)

    #     # Next, try looking up by primary key.
    #     user_id = self.kwargs.get(self.pk_url_kwarg)

    #     # if user_id is None:
    #     #     raise Http404(_('User wasn\'t found'))

    #     # If none of those are defined, it's an error.
    #     if user_id is None:
    #         raise AttributeError(
    #             f'Generic detail view {self.__class__.__name__}'
    #             ' must be called with either an object pk or a slug.'
    #             )
                
    #     queryset = queryset.filter(pk=user_id)    
    #     user = queryset.get()
        
    #     try:
    #         # Get the single item from the filtered queryset
    #         data = self.request.POST
    #         data = dict(data)
        
    #         updated_data = dict()
    #         for key, value in list(data.items())[1:]:
    #             value = ''.join(value)
    #             updated_data[key] = value

    #         user = CustomUser.update_user_by_id(
    #             user_id, 
    #             updated_data
    #         )

    #         user.save()
    #         print(user.password) # not hashed password
    #         self.success_url = f'/accounts/status-update/{user_id}'
    #         return user
            
    # except queryset.model.DoesNotExist:
    #     raise Http404(_('No %(verbose_name)s found matching the query') %
    #                 {'verbose_name': queryset.model._meta.verbose_name})
        
        
#################### *** Login/Logout Views *** ######################
def login_success_view(request, *args, **kwargs):
    messages.success(request, f'U\'ve been successfully logged in (・_・)ノ')
    return render(request, 'accounts/login_success.html', context={})

####################### *** Delete User *** #######################
def profile_delete_view(request, user_id, *args, **kwargs):
    user = get_object_or_404(CustomUser, pk=user_id)
    context = {'user': user}
    return render (request, 'accounts/delete_inquiry.html', context)

def profile_delete_submit(request, user_id, *args, **kwargs):
    CustomUser.delete_user_by_id(user_id)
    time.sleep(1.5)
    return redirect('/')

####################### *** Contact *** #######################
### Put your resume here ###
### Delete this later
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is DEV contact: NetUnit -> (095) 013 18 25 </h2>')

####################### *** Recovery *** #######################
def profile_recovery_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is recovery view -> make html+form+snippet later </h2>')

################# *** Authenticated User or Staff Member Check *** ###################
def check_user_auth(request, *args, **kwargs):
    user = request.user
    print(user)
    not_staff = user.is_staff == False
    print(user.is_authenticated, user.is_staff)
    context = {'user': user, 'not_staff': not_staff}
    print(user.is_authenticated)
    return render (request, 'user_status.html', context)


# def check_user_auth(request, *args, **kwargs):
#     user = request.user
#     context = {'user': user}
#     if not user.is_authenticated:
#         return render (request, 'not_authenticated.html', context)
#     if not user.is_staff:
#         return render (request, 'not_staff.html', context)


# def check_user_auth(request, *args, **kwargs):
#     user = request.user
#     context = {'user': user}
#     return render (request, 'not_authenticated.html', context)
    
# def check_staff_auth(request, *args, **kwargs):
#     is_staff = request.user.is_staff
#     context = {'is_staff': is_staff}
#     return render (request, 'not_staff.html', context)

def media_download_view(request, user_id, *args, **kwargs):
    '''
        downlodas media of a certain user
        :returns: HttpResponse in the form of a downloading file
                  (as oppose to render or redirect a new page)
    '''
    if not user_id:
        return redirect('/accounts/login-failed/')

    user = CustomUser.get_user_by_id(user_id)
    # or user = reauest.user
    media = user.media
    if not media:
        raise Http404
    
    user_path = media.path
    path = pathlib.Path(user_path)

    if not path.exists():
        raise Http404

    # file extension
    ext = path.suffix
    file_name = f'user-moto-picture-{user_id}{ext}'

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

#### checker
def show_info(request):
    user = request.user
    try:
        instance = auth_views.LoginView
        #print(instance.get_success_url(instance))
        # x = instance()
        # y = x.get_success_url(request)
        # print(y)
        user = request.user
        auth = request.user.is_authenticated
        staff = request.user.is_staff
        return HttpResponse(f'<h2> {user} | {auth} | {staff} <h2>')
    except Exception as err:
        print(err)

# def profile_user_view(request, user_id, *args, **kwargs):
#     try:
#         user = request.user
#         auth = request.user.is_authenticated
#         context = {'user': user, 'auth': auth}
#         return render (request, 'accounts/profile_view.html', context)
#     except Exception as err:
#         print(err)
