from django.contrib import admin
from .models import Article, Notice

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


class NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['caption']}),
        (None, {'fields': ['content']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('caption', 'content', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Notice, NoticeAdmin)
