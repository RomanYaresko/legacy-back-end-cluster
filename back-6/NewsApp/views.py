from gc import get_objects
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Article
    template_name = 'NewsApp/home.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'NewsApp/article_detail.html'
    context_object_name = 'article'


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'NewsApp/article_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'NewsApp/article_edit.html'
    context_object_name = 'form'
    fields = ('title', 'body')
    login_url = reverse_lazy('login')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'NewsApp/article_create.html'
    context_object_name = 'form'
    fields = ('title', 'body')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateCiew(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'NewsApp/comment_create.html'
    context_object_name = 'form'
    fields = ('text',)
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['article'])
        return super().form_valid(form)