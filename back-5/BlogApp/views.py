from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *


class HomeView(ListView):
    model = Post
    template_name = 'BlogApp/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'BlogApp/post.html'
    context_object_name = 'post'


class PostNewView(CreateView):
    model = Post
    template_name = 'BlogApp/new_post.html'
    fields = ['author', 'title', 'text']
    context_object_name = 'form'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'BlogApp/update_post.html'
    fields = ['title', 'text']
    context_object_name = 'form'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'BlogApp/delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')