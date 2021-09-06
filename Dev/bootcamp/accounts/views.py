from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect

from .models import CustomUser
from accounts.forms import CustomUserCreationForm
# from accounts.forms import RegisterForm
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from django.contrib import messages


################# *** Panda Hardware *** ###################
def panda_link_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is Panda website: add here info about the website </h2>')


############################## *** Full List *** ########################
def accounts_list_view(request, *args, **kwargs):
    return HttpResponse('<h2> Accounts list should be here  </h2>')


################# *** Registration *** ####################
def register_view(request, *args, **kwargs):
    try:
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            messages.success(
                request,
                f'U\'ve just created the next user: {user.name} (^_-)≡☆'
                )
            return redirect ('/accounts/register/')

        form = CustomUserCreationForm()
        context = {'form': form}
        return render (request, 'accounts/register.html', context)

    except Exception as err:
        print(err)
        pass
### will use this on the lesson#5 authentication

## Class-based View
from django.views.generic import CreateView

# class RegisterView(CreateView):
#     form_class = RegisterForm                        ### add Register Form
#     template_name = 'accounts/register.html'
#     success_url = '/contact/'

## make the same function view
#####################################################################


################# *** Authentication (Login) *** ####################
def login_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is login </h2>')
#     return render (request, 'accounts/login.html')


################# *** Contact *** ###################
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2> This is DEV contact: NetUnit -> (095) 013 18 25 </h2>')