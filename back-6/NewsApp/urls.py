from django.urls import path
from .views import *

urlpatterns = [
    path('article/<slug:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<slug:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<slug:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('comment/<slug:article>/', CommentCreateCiew.as_view(), name='comment_create'),
    path('', HomeView.as_view(), name='home'),
]
