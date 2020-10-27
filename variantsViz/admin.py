from django.contrib import admin

# Register your models here.

#from .models import Table
from .models import Job
from .models import Pathology

#admin.site.register(Table)


class JobAdmin(admin.ModelAdmin):
   list_display   = ('sample_id', 'author', 'start_date', 'running')
   list_filter    = ('author', 'running')
   date_hierarchy = 'start_date'
   ordering       = ('start_date', )
   search_fields  = ('sample_id', 'running')

admin.site.register(Job, JobAdmin)


class PathologyAdmin(admin.ModelAdmin):
   fields = ('name', 'associated_gene_OMIM', 'infos')
   list_display   = ('name', 'associated_gene_OMIM', 'infos')
   #list_filter    = ('name', 'associated_gene')
   #date_hierarchy = 'start_date'
   ordering       = ('name', 'associated_gene_OMIM')
   search_fields  = ('name', 'associated_gene_OMIM')

admin.site.register(Pathology,PathologyAdmin)

from .models import Gene

class ChoiceInline(admin.TabularInline):
    model = Pathology
    extra = 3

class GeneAdmin(admin.ModelAdmin):   
   fieldsets = [
      ('Main Information',{'fields':['name', 'OMIM_id','Ensembl_id']}),
      ('Other', {'fields': ['infos']})]
   #inlines = [ChoiceInline]
   list_display   = ('name', 'OMIM_id', 'Ensembl_id', 'infos')
   ordering       = ('name', 'Ensembl_id')
   search_fields  = ('name', 'OMIM_id', 'Ensembl_id', 'infos')

admin.site.register(Gene,GeneAdmin)


