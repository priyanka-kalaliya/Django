from django import forms
from .models import *

class Myform(forms.Form):
    name = forms.CharField(max_length=20)
    address=forms.CharField(max_length=30)
    marks = forms.IntegerField()

class Post_form(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'