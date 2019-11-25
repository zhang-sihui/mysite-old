from django.contrib import admin
from .models import Checklist


# Register your models here.

class ChecklistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['category']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
    ]
    list_display = ('title', 'category', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Checklist, ChecklistAdmin)

