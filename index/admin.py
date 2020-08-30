from django.contrib import admin
from .models import UserIP


# Register your models here.

class UserIPAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_ip']}),
        (None, {'fields': ['access_time']}),
        (None, {'fields': ['serial_number']}),
        (None, {'fields': ['ip_attribution']}),
    ]
    list_display = ('user_ip', 'access_time', 'serial_number', 'ip_attribution')
    list_filter = ['access_time']
    search_fields = ['ip_attribution']


admin.site.register(UserIP, UserIPAdmin)
