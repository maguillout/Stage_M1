from django.contrib import admin

# Register your models here.

#from .models import Table
from .models import Job
from .models import Pathology
from .models import Gene
#admin.site.register(Table)


class JobAdmin(admin.ModelAdmin):
   list_display   = ('sample_id', 'author', 'start_date', 'running')
   list_filter    = ('author', 'running')
   date_hierarchy = 'start_date'
   ordering       = ('start_date', )
   search_fields  = ('sample_id', 'running')

admin.site.register(Job, JobAdmin)


class PathologyAdmin(admin.ModelAdmin):
   fields = ('name', 'associated_genes', 'infos')
   list_display   = ('name','infos', 'initialisation_date')
#   list_filter    = ('associated_genes',)
   ordering       = ('name', 'initialisation_date')
   search_fields  = ('name',)

admin.site.register(Pathology,PathologyAdmin)



class GeneAdmin(admin.ModelAdmin):   
   fieldsets = [
      ('Main Information',{'description':'You do not have to fill the three identifiants, the others will be added automatically after saving','fields':['name', 'MIM_number','Ensembl_id']}),
      ('Other', {'fields': ['associated_pathologies','infos']})]
   #inlines = [ChoiceInline]
   list_display   = ('name', 'MIM_number', 'Ensembl_id', 'infos', 'initialisation_date')
   ordering       = ('name', 'Ensembl_id', 'initialisation_date')
   list_filter    = ('associated_pathologies',)
   search_fields  = ('name', 'MIM_number', 'Ensembl_id', 'infos', 'associated_pathologies')

admin.site.register(Gene,GeneAdmin)


from .models import Patient

class PatientAdmin(admin.ModelAdmin):   
   fieldsets = [
      ('General Information',{'fields':['identifiant', 'name','surname', 'gender', 'birth_date']}),
      ('Medical Information', {'fields': ['pathology', 'age_of_unset', 'infos']})]
   list_display   = ('identifiant', 'name','surname', 'initialisation_date')
   ordering       = ('identifiant', 'name','surname', 'age_of_unset', 'initialisation_date')
   search_fields  = ('identifiant', 'name','surname', 'pathology', 'age_of_unset', 'infos')

admin.site.register(Patient,PatientAdmin)

from .models import Variant

class VariantAdmin(admin.ModelAdmin):   
   fieldsets = [
      ('Main Information',{'fields':['rs_id','position','gene']}),
      ('Consequences',{'fields':['associated_pathologies','AAchange']}),
      ('Pathogenicity',{'fields':['ACMG_diagnostic','manual_diagnostic','CADD_score','Polyphen_score','MutationTaster_score','infos']}),
      ('Litterature',{'fields':['orphadata_link','clinvar_link']})
      ]
   #inlines = [ChoiceInline]
   list_display   = ('rs_id', 'position', 'gene', 'infos', 'initialisation_date','rs_id','gene','AAchange','manual_diagnostic','infos')
   ordering       = ('rs_id', 'position', 'gene', 'infos', 'initialisation_date','rs_id','gene','AAchange','manual_diagnostic')
   list_filter    = ('gene','associated_pathologies')
   search_fields  = ('rs_id', 'position', 'gene', 'infos', 'initialisation_date','rs_id','gene','AAchange','manual_diagnostic')

admin.site.register(Variant,VariantAdmin)


