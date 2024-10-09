from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class AuthSignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'AuthApp/signup.html'
    success_url = reverse_lazy('home')
    context_object_name = 'form'
