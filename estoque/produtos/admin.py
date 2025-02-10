from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'data_nascimento']
    search_fields = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)