####   APP2/URL.PY


from django.urls import path
from .views import *

urlpatterns = [
    path('second/', second_page, name='sec')
    ]
