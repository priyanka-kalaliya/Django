from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    d=Post.objects.all()
    if d:
        records=Post.objects.all().order_by('-id')[1:]
        last_post = Post.objects.all().order_by('-id')[0]
    else:
        records = None
        last_post = None

    # print(last_post)
    # print(records)
    return render(request,'index.html',{'rec':records,'last':last_post})

@login_required(redirect_field_name='loginapp:login')
def create_post(request):
    if request.method == 'POST':
        form = Post_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=Post_form()
    return render (request,'post.html',{'form':form})


def detail(request,d):
    r=Post.objects.get(id=d)
    return render (request,'detail.html',{'s':r})

def delete(request,m):
    z=Post.objects.get(id=m)
    z.delete()
    return redirect('index')