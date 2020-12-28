from django.contrib import admin
from django.utils.html import format_html_join
from django.contrib.admin import AdminSite
from .models import Drivers
from .models import Schedule

# class MyAdminSite(AdminSite):
AdminSite.site_header = "הסעות תלמידים עמק יזרעאל"


class DriverAdmin(admin.ModelAdmin):
    fields = ['driver_id', 'driver_name']
    list_display = ('driver_name', 'driver_id')
    search_fields = ['driver_id', 'driver_name']

class ScheduleAdmin(admin.ModelAdmin):
    fields = ['driver_id', 'start_time', 'end_time']
    list_display = ('driver_id', 'date', "hours_worked_")
    search_fields = ['driver_id__driver_name']
    #list_filter = ['date']


admin.site.register(Drivers, DriverAdmin)
admin.site.register(Schedule, ScheduleAdmin)
