from django.contrib import admin
from .models import User, Notice


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


class NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
    ]
    list_display = ('title', 'content', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Notice, NoticeAdmin)
admin.site.register(User, UserAdmin)
