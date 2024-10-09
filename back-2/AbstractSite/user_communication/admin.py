from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_image')

class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Figure)
admin.site.register(FigureBlacklist)
admin.site.register(FigureLike)
admin.site.register(Type, TypeAdmin)