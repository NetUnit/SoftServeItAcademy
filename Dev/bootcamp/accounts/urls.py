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
    ##########
    logout_success_view,
    login_success_view,
    login_failed_view,
    login_out_of_attempts_view,
    #########
    profile_user_view,
    profile_update_view,
    ########
    profile_delete_view,
    profile_delete_submit,
    ########
    show_info,
)

app_name = 'accounts'

urlpatterns = [

    re_path(r'^accounts/list/$', accounts_list_view, name='accounts_list_view'),
    
    ######################### *** REGISTER FBV + CBV *** #########################
    re_path(r'^accounts/register/$', register_user_view, name='register'),                                   ## +++ FB Registration
    re_path(r'^accounts/register2/$', RegisterView.as_view(), name='register2'),                             ## +++ CreateView

    ######################### *** LOGIN FBV + CBV *** #######################
    re_path(r'^accounts/login/$', LoginView.as_view(), name='login'),
    re_path(r'^accounts/login2/$', login_user_view, name='login_fbw'),                                       ## +++ authenticate doesn't work - set_apssword()
    re_path(r'^accounts/login-success/$', login_success_view, name='login-success'),                         ## +++
    re_path(r'^accounts/login-failed/$', login_failed_view, name='login_failed'),                            ## +++
    re_path(r'^accounts/login-out-of-attempts/$', login_out_of_attempts_view, name='login_out_of_attempts'), ## +++
    
    ######################### *** LOGOUT CBV *** #######################
    re_path(r'^accounts/log-out/', logout_success_view, name='logout'),                                              ## ++

    ######################### *** profile FBW ***#######################
    re_path(r'^accounts/profile/$', profile_user_view, name='profile'),                                      ## ++

    ######################### *** profile DELETE FBW ***#######################
    re_path(r'^accounts/profile-delete/(?P<user_id>\d+)/$', profile_delete_view, name='profile_delete_view'),            ## ++
    re_path(r'^accounts/profile-delete-submit/(?P<user_id>\d+)/$', profile_delete_submit, name='profile_delete_submit'), ## ++

    ######################### *** UPDATE CBV *** #######################
    path(r'<int:pk>/edit-profile-page/', EditProfilePageView.as_view(), name='edit_profile_page_view'),        ## ++
    re_path(r'^accounts/profile-update/(?P<user_id>\d+)/$', profile_update_view, name='profile_update_view'),  ## -- redefine forms.Form

    ######### *** show info *** #########
    re_path(r'^accounts/show-info/$', show_info, name='show_info'), 
]