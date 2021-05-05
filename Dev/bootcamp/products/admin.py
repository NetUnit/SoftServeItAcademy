from django.contrib import admin

# Register your models here.
from .models import Product


from django.contrib.auth.admin import UserAdmin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    ordering = ['id']
    list_display = ('id', 'title', 'content', 'price')

    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fields': ('id', 'title', 'content', 'price')}),
        )


# admin.site.register(Product)