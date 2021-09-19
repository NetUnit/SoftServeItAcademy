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
    ##########
    profile_user_view,
    profile_update_view,
    profile_delete_view,
)

app_name = 'accounts'

urlpatterns = [

    re_path(r'^accounts/list/$', accounts_list_view, name='accounts_list_view'),
    
    ######################### *** REGISTER FBV + CBV *** #########################
    re_path(r'^accounts/register/$', register_user_view, name='register'),
    re_path(r'^accounts/register2/$', RegisterView.as_view(), name='register2'), ## CreateView

    ######################### *** LOGIN FBV + CBV *** #######################
    re_path(r'^accounts/login/$', LoginView.as_view(), name='login'),
    re_path(r'^accounts/login2/$', login_user_view, name='login-fbw'),
    
    ##############################################################################
    re_path(r'^accounts/profile/$', profile_user_view, name='profile'),
    re_path(r'^accounts/profile-update/(?P<user_id>\d+)/$', profile_update_view, name='profile_update_view'),
    re_path(r'^accounts/profile-delete/(?P<user_id>\d+)/$', profile_delete_view, name='profile_delete_view'),

]