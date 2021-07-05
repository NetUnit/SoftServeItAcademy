from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
# Create your views here.

from .models import Emails
############################## *** Full List *** ###############################
def emails_list_view(request, *args, **kwargs):
    return HttpResponse('<h2>Should be the email\'s list here </h3>')
