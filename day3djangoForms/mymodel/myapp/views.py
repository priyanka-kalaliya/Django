from django.shortcuts import render
from . models import *
from django.http import *
from .forms import *

# Create your views here.
def add_record(request):
    if request.method=='POST':
        form = Myform(request.POST)
        if form.is_valid():
            d=form.cleaned_data
            print(d)
            n=d['name']
            a=d['address']
            m=d['marks']

            q=student_info(name=n,address=a,marks=m)
            q.save()
            
            return HttpResponseRedirect('/')
        pass
    else:
        form = Myform()
    return render(request,'stuform.html',{'form':form})    




        

def del_records(request,x):
    z=student_info.objects.get(id=x)
    z.delete()
    return HttpResponseRedirect('/')

def index(request):
    records = student_info.objects.all()
    print(records)
    context_dict = {'info': records}
    return render(request, 'index.html', context_dict)