from django.contrib import admin

# Register your models here.
from .models import Product
from django.contrib.auth.admin import UserAdmin
# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    ordering = ['id']
    list_display = ('id', 'title', 'content', 'price', 'image' , 'media')

    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fields': ('id', 'title', 'content', 'price')}),
        )
