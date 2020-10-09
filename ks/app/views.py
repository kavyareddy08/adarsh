from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib import messages
from .models import Contact
from django.core import mail
from django.core.mail.message import EmailMessage




# Create your views here.
def index(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def handleBlog(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request,'handleBlog.html')

def services(request):
    return render(request,'services.html')

    
def contact(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('num')
        description=request.POST.get('desc')
        contact_query=Contact(name=fullname,email=email,number=phone,description=description)
        contact_query.save()
        from_email=settings.EMAIL_HOST_USER
        # email starts here
        # your mail starts here
        connection=mail.get_connection()
        connection.open()
        email_mesge=mail.EmailMessage(f'Website Email from {fullname}',f'Email from : {email}\nUser Query :{description}\nPhone No : {phone}',from_email,['kavyareddysr07@gmail.com','snsathya7411@gmail.com'],cc=[],connection=connection)
        email_user=mail.EmailMessage('KAVYA',f'Hello {fullname}\nThanks fo Contacting Us Will Resolve Your Query Asap\nThank You',from_email,[email],connection=connection)
        connection.send_messages([email_mesge,email_user])
        connection.close()
        messages.info(request,"Thanks for Contacting Us ")
        return redirect('/contact')

    return render(request,'contact.html')
    

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
    messages.success(request,"logout succesfull")
    return redirect('/login')