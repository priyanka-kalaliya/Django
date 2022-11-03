from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.http import *


# Create your views here.
def user_login(request):
    if request.method =='POST':
        email = request.POST.get('email',None)
        pwd = request.POST.get('password',None)     

        user_object=User.objects.get(email=email)
        user=authenticate(username=user_object.username,password=pwd)

        if user is not None:
            login(request,user)
            return redirect('login_page')
        else:
            return HttpResponse('Invalid username/password')

    return render(request,'index.html')


def index(request):
    return render(request,'home.html')


def home(request):
    if request.user.is_authenticated:
        return index(request)
    else:
        return user_login(request)


def register(request):
    if request.method=='POST':
        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        pwd = request.POST.get('password',None)

        User.objects.create_user(username=username,email=email,password=pwd)

        return redirect('login_page')

    return render(request,'register.html')