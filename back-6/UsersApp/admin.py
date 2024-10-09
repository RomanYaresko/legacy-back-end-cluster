from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreatinForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email' , 'age', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)