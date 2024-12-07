from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import FileForm
from .models import File
from .models import *
from django.contrib.auth.models import User
import os
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

def e_logout(request):
    logout(request)  
    return redirect(e_login)
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
    

def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')  
    else:
        form = FileForm()
    
    return render(request, 'file_add.html', {'form': form})


def file_list(request):
    
    files = File.objects.all()
    
    
    return render(request, 'file_view.html', {'files': files})



def delete_file(request, file_id):
    # Get the file object using its ID
    file_to_delete = get_object_or_404(File, id=file_id)

    # Optionally, delete the actual file from the filesystem
    if file_to_delete.file:
        file_path = file_to_delete.file.path
        if os.path.exists(file_path):
            os.remove(file_path)
    
    # If there's an associated image, delete it from the filesystem
    if file_to_delete.image:
        image_path = file_to_delete.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
    
    # If there's an associated video, delete it from the filesystem
    if file_to_delete.video:
        video_path = file_to_delete.video.path
        if os.path.exists(video_path):
            os.remove(video_path)

    # Delete the file record from the database
    file_to_delete.delete()

    # Add a success message
    messages.success(request, "File deleted successfully.")

    # Redirect to the file list page
    return redirect('file_list')




def home(req):
    return render(req,'home.html')