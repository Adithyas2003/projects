from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def e_shop_login(req):
    if 'shop' in req.session:
        return redirect(home)
    if 'user' in req.session:
        return redirect(home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=uname
                return redirect(home)
            else:
                req.session['user']=uname
                return redirect(home)
        else:
            messages.warning(req, "invalid password")
            return redirect(e_shop_login)
    else:
        return render(req,'home.html')
def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
           
            Contact.objects.create(name=name, email=email, message=message)
            
            return HttpResponse("Thank you for your message. We'll get back to you soon.", content_type="text/plain")
        else:
            
            return HttpResponse("Please fill in all fields.", content_type="text/plain")

    return render(request, 'contact.html')  

def about(request):
    return render(request,'about.html')

def courses(request):
    data=Courses.objects.all()
    return render(request,'courses.html',{'courses':data})


def details(req,cid):
    if req.method=='POST':
        name=req.POST['name']
        dis=req.POST['dis']
       
        data=Contact.objects.create(name=name,dis=dis)
