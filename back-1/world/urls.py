from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', HelloUser, name="hello")
]
