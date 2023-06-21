from django.shortcuts import render, redirect,HttpResponse
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
    return render(request,'index.html')

def removePunc(request):
    s = request.GET.get('text','default')
    return HttpResponse("The text you've entered is : " + s)
    # context = {
    #     'variable': "this is sent"
    # }
    # return render(request,'index.html',context)
    # # return HttpResponse("this is homepage")
# def loginUser(request):
#     if request.method == "POST":
#         #check credit
#         username = request.POST.get('userName')
#         password = request.POST.get('passWord')
#         print(username,password,"TWO")
#         user = authenticate(username = userName , password = passWord)
#         if user is not None:
#             login(request,user)
#             return redirect("/")
#         else:
#             return render(request,'login.html') 
#     return render(request,'login.html') 
# def logoutUser(request):
#     logout(request)
#     return redirect("/login")
