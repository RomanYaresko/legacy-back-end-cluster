from django.urls import path
from .views import *

urlpatterns = [
    path('post/<slug:pk>/delete', PostDeleteView.as_view(), name='delete_post'),
    path('post/<slug:pk>/update', PostUpdateView.as_view(), name='update_post'),
    path('post/new/', PostNewView.as_view(), name='new_post'),
    path('post/<slug:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('', HomeView.as_view(), name='home'),
]
