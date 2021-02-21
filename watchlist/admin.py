from django.contrib import admin
from .models import Watchlist


# Register your models here.

class WatchlistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['category']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['content']}),
    ]
    list_display = ('title', 'category', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Watchlist, WatchlistAdmin)
