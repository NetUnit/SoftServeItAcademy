from django.contrib import admin

# Register your models here.
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    ordering = ['id']
    list_display = ('id', 'email',
                    'password', 'nickname',
                    'first_name', 'last_name')

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('id', 'email', 'password', 'nickname')}),
    )