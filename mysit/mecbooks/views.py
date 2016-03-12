
from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext, loader
# from bloodbank.forms import *
# #from login.forms import *
# from django.contrib.auth.models import User
# #from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
# #from django.views.decorators.csrf import csrf_protect
# from django.shortcuts import render_to_response
# from django.http import HttpResponseRedirect
# from django.template import RequestContext
# from django.contrib.auth import authenticate, login
# from bloodbank.models import *
# from django.template import Context, Template

def index(request):
    return HttpResponse("Welcome to mec online book library ")

