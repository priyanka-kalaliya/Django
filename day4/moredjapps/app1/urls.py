####   APP1/URL.PY

from django.urls import path, re_path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    re_path('edit/(\d+)/',edit_record,name='edit'),
    re_path('delete/(\d+)/',delete_record,name='delete'),
    re_path('post/(\d+)/',display_post,name='single_post')
]
