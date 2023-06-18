from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
# Create your views here.


def about(request):
    return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services")

def contacts(request):
    return HttpResponse("this is contacts")

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    # context = {
    #     'variable': "this is sent"
    # }
    # return render(request,'index.html',context)
    # # return HttpResponse("this is homepage")
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        #check credit
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html') 
    return render(request,'login.html') 
def logoutUser(request):
    logout(request)
    return redirect("/login")