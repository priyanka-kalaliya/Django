from django import forms
from .models import *
from django.contrib.auth.models import User

class Registration_form(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','first_name','email','password']


class Post_form(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'