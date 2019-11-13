from django.contrib import admin
from .models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['password']})
    ]
    list_display = ('username', 'create_time', 'was_created_recently')
    list_filter = ['create_time']
    search_fields = ['username']


admin.site.register(User, UserAdmin)
