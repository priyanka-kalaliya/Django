from django import forms

class Myform(forms.Form):
    name = forms.CharField(max_length=20)
    address=forms.CharField(max_length=30)
    marks = forms.IntegerField()