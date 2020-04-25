from django.contrib import admin
from .models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['password']}),
        (None, {'fields': ['register_code']}),
    ]
    list_display = ('username', 'email', 'create_time', 'register_code')
    list_filter = ['create_time']
    search_fields = ['username']


admin.site.register(User, UserAdmin)
