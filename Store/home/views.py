from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services")

def contacts(request):
    return HttpResponse("this is contacts")

def login(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')