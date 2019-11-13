from django.contrib import admin
from .models import Article, Notice

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['category']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['body']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']


class NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['notice']}),
        (None, {'fields': ['content']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('notice', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Notice, NoticeAdmin)
