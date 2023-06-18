from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import users
from django.contrib.auth import logout,authenticate
# Create your views here.


def about(request):
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services")

def contacts(request):
    return HttpResponse("this is contacts")

def index(request):
    if request.user.anonymous:
        return redirect("/login")
    # context = {
    #     'variable': "this is sent"
    # }
    # return render(request,'index.html',context)
    # # return HttpResponse("this is homepage")

def login(request):
    if request.method == "POST":
        #check credit
        username = request.POST.get('username')
        password = request.POST.get(password)
        user = authenticate(username = username , password = password)
        if user is not None:
            return redirect("/")
        else:
            return render(request,'login.html') 
    return render(request,'login.html') 
def logout(request):
    logout(request)
    return redirect("/login")