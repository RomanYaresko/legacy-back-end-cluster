from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreatinForm

class SignUpView(CreateView):
    form_class = CustomUserCreatinForm
    success_url = reverse_lazy('login')
    template_name = 'UsersApp/signup.html'