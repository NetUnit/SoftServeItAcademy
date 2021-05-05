from django.contrib import admin

# Register your models here.
from .models import Profile


admin.site.register(Profile)

## transfer to authetication after
# from django.contrib.auth.admin import UserAdmin

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     model = Profile
#     ordering = ['id']
#     content = ('id', 'content')

#     add_fieldsets = UserAdmin.add_fieldsets + (
#             (None, {'fields': ('id', 'content')}),
#         )
