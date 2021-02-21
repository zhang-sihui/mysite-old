from django.contrib import admin
from .models import File


# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'pub_date', 'downloads_count')
    list_filter = ['pub_date']
    search_fields = ['file_name']


admin.site.register(File, FileAdmin)
