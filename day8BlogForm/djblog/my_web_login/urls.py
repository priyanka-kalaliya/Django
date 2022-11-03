
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='login'),
    path('register/', user_register, name='register'),
    path('logout/',logout_user,name='logout'),
    path('user_auth/',user_auth,name='userauth'),

]
