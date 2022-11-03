from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    rec=Product.objects.all()
    return render(request,'index.html',{'rec':rec})


def product_detail(request,d):
    item=Product.objects.get(id=d)
    return render(request,'detail.html',{'item':item})