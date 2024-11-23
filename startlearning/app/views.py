from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

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
    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')