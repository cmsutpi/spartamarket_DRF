from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField()
    email = forms.EmailField()