import email
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def user_login(request):

    return render (request,'login.html')


@require_http_methods(['POST'])
def user_auth(request):    
    uname=request.POST.get('username')
    pwd=request.POST.get('password')

    user=authenticate(username=uname, password=pwd)

    if user is not None:
        login(request, user)
        return redirect('login')
    else:
        return HttpResponse ('Username/Password incorrect')   


def index_page(request):
    if request.method=='POST':
        form = Post_form(request.POST)
        if form.is_valid():
            form.save()            
            return HttpResponseRedirect('/')
    else:
        form = Post_form()
        records = Post.objects.all()
    return render(request,'stuform.html',{'form':form,'rec':records})    

    # return render(request, 'index.html')


def home(request):
    if request.user.is_authenticated:
        return index_page(request)
    else:
        return user_login(request)


def logout_user(request):
    logout(request)
    return redirect('login')


def user_register(request):
    if request.method=='POST':
        form = Registration_form(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            fn = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            psw = form.cleaned_data['password']
            User.objects.create_user(username=un,first_name=fn, email=email,password=psw)

            return redirect('login')
    else:
        form = Registration_form()
    return render(request,'register.html',{'form':form})