from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services")