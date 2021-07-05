# from django.conf.urls.static import static
from django.urls import path, re_path
from emails.views import (
    emails_list_view
    )

app_name = 'emails'

urlpatterns = [

    re_path(r'^emails/list/$', emails_list_view, name='emails_list_view'),

] 