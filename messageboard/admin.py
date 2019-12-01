from django.contrib import admin
from .models import MessageBoard


# Register your models here.
class MessageBoardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['message']}),
        (None, {'fields': ['sub_date']}),
        (None, {'fields': ['reply']}),
    ]
    list_display = ('message', 'sub_date')
    list_filter = ['sub_date']
    search_fields = ['message']


admin.site.register(MessageBoard, MessageBoardAdmin)