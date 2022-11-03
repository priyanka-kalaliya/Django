
from django import forms
from .models import *

# Create your models here.
class author_form(forms.ModelForm):
    class Meta:
        model = Author
        fields='__all__'


class book_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'