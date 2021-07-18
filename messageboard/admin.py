from django.contrib import admin
from .models import MessageBoard


# Register your models here.

class MessageBoardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['content']}),
        ('Date information', {'fields': ['sub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['reply']}),
        (None, {'fields': ['reply_date']}),
    ]
    list_display = ('id', 'sub_date', 'username', 'content')
    list_filter = ['sub_date']
    search_fields = ['content']


admin.site.register(MessageBoard, MessageBoardAdmin)
