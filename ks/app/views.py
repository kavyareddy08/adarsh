
from django.shortcuts import render,HttpResponse,redirect
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,'index.html')

def handleBlog(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    return render(request,'handleBlog.html')

def services(request):
    return render(request,'services.html')

    
def contact(request):
    return render(request,'contact.html')
    
def about(request):
    return render(request,'about.html')

def signup(request):

    if request.method=="POST":
            username=request.POST['username']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email=request.POST['email']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            if pass1!=pass2:

                return HttpResponse("Password not match")


            try:
                 if User.objects.get(username=username):
                     return HttpResponse("username is taken")

            except Exception as identifier:
                 pass

            myuser=User.objects.create_user(username,email,pass1) 
            myuser.first_name=firstname
            myuser.last_name=lastname
            myuser.save()
            return HttpResponse("signup successful")  

    return render(request,'auth/signup.html')

def handlelogin(request):
    if request.method=="POST":
        handleusername=request.POST['username']
        handlepassword=request.POST['pass1']
        user=authenticate(username=handleusername,password=handlepassword)
        if user is not None:
            login(request,user)
            messages.info(request,"welcome to my website")
            return redirect('/')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('/login')
            return HttpResponse("Invalid Credentials")
   
    return render(request,'auth/login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"logout succesful")
    return redirect('/login')