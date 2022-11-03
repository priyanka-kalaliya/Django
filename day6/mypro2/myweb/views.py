from django.shortcuts import render
from .models import *
from django.http import *
from .forms import *

# Create your views here.
def index(request):

    d = Book.objects.all()

    return render(request,'home.html',{'info':d})

def authorform(request):
    if request.method=='POST':
        form=author_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        pass
    else:
        form = author_form()
    return render(request,'author.html',{'form':form})


def bookform(request):
    if request.method=='POST':
        form = book_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        pass
    else:
        form = book_form()
    return render(request,'book.html',{'form':form})