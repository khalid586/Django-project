from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
# Create your views here.


# def about(request):
#     return HttpResponse("this is about")

# def services(request):
#     return HttpResponse("this is services")

# def contacts(request):
#     return HttpResponse("this is contacts")
def ex1(request):
    s = ''' <a href = "https://www.facebook.com/">Facebook</a> <br> 
            <a href = "https://www.google.com/">Google</a> <br>
            <a href = "https://www.amazon.com/">amazon</a>
    '''
    return HttpResponse(s)

def index(request):
    return render(request,'index.html')

def analyze(request):
    Text = request.GET.get('text','default')
    rmvPunc = request.GET.get('removePunc','off')
    capital = request.GET.get('upperCase','off')
    charCnt = request.GET.get('CharCount','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    final = ''''''
    
    if rmvPunc == 'on':
        for ch in Text:
            if ch not in punctuations:
                final = final + ch
        params = {'purpose':'Remove Punctuation','analyzed_text':final}
        return render(request,'analyze.html',params)
    elif capital == 'on':
        for ch in Text:
            if ch not in punctuations:
                final = final + ch.upper()
        params = {'purpose':'Capitalization','analyzed_text':final}
        return render(request,'analyze.html',params)
    
    elif charCnt == 'on':
        cnt = 0
        for ch in Text:
            if ch not in punctuations:
                if ch != ' ':
                    cnt += 1
        params = {'purpose':'Character count','analyzed_text':cnt}
        return render(request,'analyze.html',params)
        
    else:
        return render(request,'analyze.html',Text)


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
