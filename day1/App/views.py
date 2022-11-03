from django.shortcuts import render
from django.http import *
import datetime

# Create your views here.
def home (request):
    # return HttpResponse("Hello World")

    # d=[1,2,3,4,5]
    # k={'info':d}
    dt = datetime.datetime.today()
    k = {"info": dt}
    return render(request,'index.html',k)

def second_page(request):
    return render(request,'second.html')