
from django.shortcuts import render,redirect,HttpResponse
from .models import Register


# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == "POST":
       fullname=request.POST.get('fullname')
       email=request.POST.get('Email')
       phonenumber=request.POST.get('PhoneNumber')
       state=request.POST.get('State')
       gender=request.POST.get('gender')
       print(fullname,email,phonenumber,state,gender)
      
       query=Register (fullname=fullname,email=email,phonenumber=phonenumber,state=state,gender=gender)
       query.save()
       return HttpResponse("Registration Succesfull")
    
    return render(request,'index.html')

    

