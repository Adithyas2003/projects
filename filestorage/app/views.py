from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def e_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            return redirect(home)
        
        else:
            messages.warning(req, "invalid password")
            return redirect(e_login)
    else:
        return render(req,'login.html')
def register(req):
    if req.method=='POST':
        username=req.POST['uname']
        email=req.POST['email']
        password=req.POST['pswd']
        
        
        try:
            data=User.objects.create_user(first_name=username,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req,"username already exist")
            return redirect(register)
        return redirect(e_login)
    else:
        return render(req,'register.html')
    



def home(req):
    return render(req,'home.html')