from django.contrib import admin

# Register your models here.
from .models import Order
from django.contrib.auth.admin import UserAdmin

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    ordering = ['id']

    list_display = ('product', 'created_at', ) ## add user later

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('id', 'product', 'created_at')}),
    )