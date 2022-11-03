from django import forms
from .models import *

# Create your models here.
class Post_form(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'