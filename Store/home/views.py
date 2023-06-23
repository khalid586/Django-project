from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
# Create your views here.
def index(request):
    return HttpResponse('this is home index')