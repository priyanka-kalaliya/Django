from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def second_page(request):
    if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('demoapp1:index')
        pass
    else:
        form=Myform()
    return render(request, 'second.html',{'form':form})

    # return render(request, 'second.html')
