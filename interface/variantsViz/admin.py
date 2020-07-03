from django.contrib import admin

# Register your models here.

from .models import Table
from .models import Job

admin.site.register(Table)


class JobAdmin(admin.ModelAdmin):
   list_display   = ('sample_id', 'author', 'start_date', 'running')
   list_filter    = ('author', 'running')
   date_hierarchy = 'start_date'
   ordering       = ('start_date', )
   search_fields  = ('sample_id', 'running')

admin.site.register(Job, JobAdmin)