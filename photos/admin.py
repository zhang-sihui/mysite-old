from django.contrib import admin
from .models import Photo


# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['photo_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('photo_name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['photo_name']


admin.site.register(Photo, PhotoAdmin)
