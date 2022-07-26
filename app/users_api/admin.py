from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
    
    list_display = (
        'user', 'username', 'first_name', 'last_name', 'email', 'profile'
    )