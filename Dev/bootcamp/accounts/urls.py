# from django.conf.urls.static import static
from django.conf.urls import include

from django.urls import path, re_path
from accounts.views import (
    accounts_list_view,
    #########
    register_user_view,
    RegisterView,
    #########
    login_user_view,
    LoginView,

)

app_name = 'accounts'

urlpatterns = [

    re_path(r'^accounts/list/$', accounts_list_view, name='accounts_list_view'),
    ######################### *** LOGIN FBV + CBV *** #######################
    re_path(r'^accounts/login2/$', login_user_view, name='login2'),
    re_path(r'^accounts/login/$', LoginView.as_view(), name='login'),


    ######################### *** REGISTER FBV + CBV *** #########################
    re_path(r'^accounts/register/$', register_user_view, name='register'),
    re_path(r'^accounts/register2/$', RegisterView.as_view(), name='register2'), ## CreateView
]