from cProfile import label
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ImageField, ModelForm

class UserReg(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form_input'}), min_length=3, max_length=20, label="User name")
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form_input'}), min_length=3, max_length=20, label="First name")
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form_input'}), min_length=3, max_length=20, label="Last name")
    password1 = forms.CharField(widget = forms.TextInput(attrs={'class': 'form_input', 'type':'password'}), label = "Password")
    password2 = forms.CharField(widget = forms.TextInput(attrs={'class': 'form_input', 'type':'password'}), label = "Password again")
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form_input'}), label="Email")
    user_image = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_image']

class UserLog(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form_input', 'id': 'username_login'}), min_length=3, max_length=20, label="User name")
    password = forms.CharField(widget = forms.TextInput(attrs={'class': 'form_input', 'type':'password'}), label = "Password")

class MakeFigure(ModelForm):
    class Meta:
        model = Figure
        fields = ["title", "type", "image", "text", "cost", "slug"]
