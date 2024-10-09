from django.shortcuts import render
from django.views.generic import ListView
from .models import * 

class ShowPosts(ListView):
    template_name = 'posts/home.html'
    model = Post
    context_object_name = 'all_posts'
