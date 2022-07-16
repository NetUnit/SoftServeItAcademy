from django.contrib import admin

# Register your models here.
from .models import Manufacturer
from django.contrib.auth.admin import UserAdmin


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    ordering = ['id']
    list_display = ('title', 'country', 'year', 'image', 'media')

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('id', 'title',
                           'country', 'year',
                           'image', 'media')}), )
