from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', AuthSignupView.as_view(), name='signup'),
]
