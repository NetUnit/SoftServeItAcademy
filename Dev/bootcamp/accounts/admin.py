from django.contrib import admin

# Register your models here.
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    ordering = ['id']
    list_display = ('id', 'username', 
                    'is_staff', 'email',
                    'first_name', 'last_name',
                    'image', 'media')

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('id', 'username', 'is_staff',
                           'username', 'first_name',
                           'last_name', 'image', 'media')}))
