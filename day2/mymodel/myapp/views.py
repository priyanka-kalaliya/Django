from django.shortcuts import render
from . models import *
from django.http import *


def index(request):
    d=post.objects.all()

    for i in d:
        print(i.tittle)
        print(i.text)
    return HttpResponse('Hello')
    return render(request, 'index.html', context_dict)

    # Priya
    # priya@gmail.com
    # 9587499937