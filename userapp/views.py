from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
import requests
from .models import plantModel
from . import celery_func
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

def xml_parser(request):
    if request.method == "POST":
        print(request.user.username)
        xml_file_link = request.POST.get("xml_link")
        celery_func.check_xml_file.apply_async(queue='celery_worker',args=[xml_file_link,request.user.username])
        return render(request,"dashboard.html")

    else:
        return render(request,"dashboard.html")


def login_user(request):
    if request.user.is_authenticated:
        return render(request,"dashboard.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        check_user = authenticate(username = username,password = password)
        print(check_user)
        if check_user:
            return render(request,"dashboard.html")
        else:
            return render(request,"login.html",{"error":"This user not found"})
    else:
        return render(request,"login.html")
def logout_user(request):
    logout(request)
    return render(request,"login.html")

    

def signUp(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            return render(request,"signUp.html",{"error":"This username is already in use"})
        password = request.POST.get("password")
        email = request.POST.get("email")
        if User.objects.filter(email = email).exists():
            return render(request,"signUp.html",{"error":"This email is already in use"})
        new_user = User(username=username,email=email)
        new_user.set_password(password)
        new_user.save()
                                                            
        return redirect("/login/")
    else:
        return render(request,"signup.html")

def dashboard(request):
    return render(request,"dashboard.html")