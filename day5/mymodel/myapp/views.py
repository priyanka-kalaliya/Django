from django.shortcuts import render
from . models import *
from django.http import *
from .forms import *

# Create your views here.
def add_record(request):
    if request.method=='POST':
        form = Post_form(request.POST)
        if form.is_valid():
            # d=form.cleaned_data

            form.save()
            
            return HttpResponseRedirect('/')
        pass
    else:
        form = Post_form()
    return render(request,'stuform.html',{'form':form})    




        

def del_records(request,x):
    z=Post.objects.get(id=x)
    z.delete()
    return HttpResponseRedirect('/')

def index(request):
    records = Post.objects.all()
    print(records)
    context_dict = {'info': records}
    return render(request, 'index.html', context_dict)