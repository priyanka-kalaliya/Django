from django.db import models
from django import forms

from app1.models import *

class Myform(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'

# Create your models here.
