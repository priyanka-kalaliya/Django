from django.shortcuts import render,redirect
from .models import *
from app2.forms import *

# Create your views here.
def index(request):
    r=Post.objects.all()
    return render(request, 'home.html',{'d':r})

def edit_record(request,d):
    z=Post.objects.get(id=d)
    if request.method=='POST':
        form=Myform(request.POST,instance=z)
        if form.is_valid():
            form.save()
            return redirect('demoapp1:index')
        pass

    else:
        form=Myform(instance=z)
        return render(request, 'update.html', {'form':form})

def delete_record(request,x):
    z=Post.objects.get(id=x)
    z.delete()
    return redirect('demoapp1:index')

def display_post(request,d):
    n=Post.objects.get(id=d)
    return render(request,'singlepost.html',{'n':n})