from django.shortcuts import render
from . models import *
from django.http import *

# Create your views here.

def index(request):
    records = post.objects.all()
    print(records)
    context_dict = {'info': records}
    return render(request, 'index.html', context_dict)


    # #crud operation


    # # create record
    # '''stu_object = student_info(name ='john', address='d',marks=345)
    # stu_object.save()'''
    # records = student_info.objects.all()
    # print(records)
    # context_dict = {'info': records}



    # ## fetch records


    # # records = student_info.objects.all()
    # # records = student_info.objects.filter(name='john')
    # # records = student_info.objects.filter(name_contains='john')

    # # Post.object.get(id=2)
    # # records = student_info.objects.all()
    # # print(records)
    # context_dict = {'info': records}



    # #delete


    # '''q = student_info.objects.get(id=5)
    # q.delete()
    # '''
    # records = student_info.objects.all()
    # print(records)
    # context_dict = {'info': records}



    # ##update


    # '''q = student_info.objects.get(id=3)
    # q.address = 'new address'
    # q.save()
    # '''

    # records = student_info.objects.all()
    # print(records)
    # context_dict = {'info': records}

    # # for i in records:
    # #     print(i.tittle)
    # #     print(i.text)
    # # return HttpResponse('Hello')
    # return render(request, 'index.html', context_dict)



def del_records(request,x):
    z=student_info.objects.get(id=x)
    z.delete()
    return HttpResponseRedirect('/')