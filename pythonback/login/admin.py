from django.contrib import admin

from login.models import *

# Register your models here.


admin.site.site_title = '座位预约系统'
admin.site.site_header = '座位预约系统'
admin.site.index_title = '座位预约系统'


class StudentsManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('name', 'phone')
    list_display = ['id', 'name', 'password', 'phone', 'email', 'time', 'is_active', 'admin_sample']


class RoomsManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('name',)
    list_display = ['id', 'name', 'capacity', 'photo', 'open_time', 'close_time', 'is_active']

    list_editable = ['name', 'capacity', 'photo', 'open_time', 'close_time', 'is_active']


admin.site.register(Room, RoomsManager)
