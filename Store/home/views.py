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
    s = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
        ]
    return HttpResponse(s)

def index(request):
    return render(request,'index.html')

def analyze(request):
    Text = request.POST.get('text','default')
    rmvPunc = request.POST.get('removePunc','off')
    capital = request.POST.get('upperCase','off')
    charCnt = request.POST.get('CharCount','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    final = ''''''
    params = {'purpose':'' , 'analyzed_text':''}
    
    if rmvPunc == 'on':
        for ch in Text:
            if ch not in punctuations:
                final = final + ch
        params['purpose'] = 'remove punctuation'
        params['analyzed_text'] = final
       # return render(request,'analyze.html',params)
       
    else:
        final = Text
    
    if capital == 'on':
        for ch in Text:
                final = final.upper()
        if rmvPunc == 'on':
            params['purpose'] += ' and capitalization'
        else:
            params['purpose'] += 'capitalization'
            
        
        params['analyzed_text'] = final
        #return render(request,'analyze.html',params)
      
    elif final == '':
        final = Text
    
    if charCnt == 'on':
        cnt = 0
        for ch in final:
            if ch != ' ':
                cnt += 1
        
        if rmvPunc == 'on' or capital == 'on':
            params['purpose'] += ' and character count'
        else:
            params['purpose'] += 'character count'
            
        params['analyzed_text'] = final + ' Character count is = ' + str(cnt)
    if(capital != 'on' and rmvPunc != 'on' and charCnt != 'on'):
        return HttpResponse("<h1> <b> Error!!!  You have not given any instruction</b> </h1>")
    
    return render(request,'analyze.html',params)


    # context = {
    #     'variable': "this is sent"
    # }
    # return render(request,'index.html',context)
    # # return HttpResponse("this is homepage")
# def loginUser(request):
#     if request.method == "POST":
#         #check credit
#         username = request.POST.POST.get('userName')
#         password = request.POST.POST.get('passWord')
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
