# from django.conf.urls.static import static
from django.conf.urls import include

from django.urls import path, re_path
from accounts.views import (
    EditProfilePageView,
    accounts_list_view,
    #########
    register_user_view,
    RegisterView,
    #########
    login_user_view,
    LoginView,
    set_password,
    ##########
    logout_view,
    #########
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
    re_path(r'^accounts/login2/$', login_user_view, name='login-fbw'),                                       ## authenticate doesn't work - set_apssword()
    re_path(r'^accounts/set-password/$', set_password, name='set_password'), 
    
    ######################### *** LOGOUT CBV *** #######################
    re_path(r'^accounts/log-out/', logout_view, name='logout'),                                              ## ++

    ##############################################################################
    re_path(r'^accounts/profile/$', profile_user_view, name='profile'),
    re_path(r'^accounts/profile-update/(?P<user_id>\d+)/$', profile_update_view, name='profile_update_view'), ## -- redefine forms.Form
    re_path(r'^accounts/profile-delete/(?P<user_id>\d+)/$', profile_delete_view, name='profile_delete_view'), ## ++

    ## update 2
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page_view'),        ## ++
    

]