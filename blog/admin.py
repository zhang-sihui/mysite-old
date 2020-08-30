from django.contrib import admin
from .models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['author']}),
        (None, {'fields': ['category']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['body']}),
    ]
    list_display = ('title', 'author', 'category', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
