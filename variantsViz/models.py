from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#models.ForeignKey -> lien vers un autre modèle

# class Table(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     sample_id = models.CharField(max_length=200)
#     path_file = models.CharField(max_length=200)
#     real_path_file = models.FilePathField(path='/home/maelle/Bureau/Stage/Data')
#     #text = models.TextField()
#     tab = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.sample_id

#     def importation(self):
#         self.tab=pd.read_csv(self.path_file, sep =';')



class Job(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sample_id = models.CharField(max_length=200)
    real_path_file = models.FilePathField(path='/home/maelle/Bureau/Stage/Data')
    #info = models.TextField(default=None)
    start_date = models.DateTimeField(default=timezone.now)
    running = models.BooleanField(default=True)    

    def __str__(self):
        return self.sample_id

class variantsTable(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sample_id = models.CharField(max_length=200)
    path_file = models.CharField(max_length=200)
    real_path_file = models.FilePathField(path='/home/maelle/Bureau/Stage/Data')
    #text = models.TextField()
    tab = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sample_id

class Pathology(models.Model):  #implementation of the object "pathology"
    #attributes required to add a new pathology
    name = models.CharField(max_length=200, unique=True)
    associated_gene_OMIM = models.CharField(max_length=20)
    infos = models.TextField(blank=True, verbose_name="Other information")
    #associated_gene = models.ForeignKey('Gene',on_delete=models.CASCADE) 
    #on_delete defines consequences of suppression of the gene, with models.SET_NULL the gene field will be empty  

    class Meta:
        #definition of the plural name (by default, adds a 's')
        verbose_name = "Pathologie"  

    def __str__(self):
        #prints the pathology (its name)
        return (self.name)


class Gene(models.Model): 
    #attributes required to add a new gene to the database

    name = models.CharField(default="",max_length=200, blank=True)
    OMIM_id = models.CharField(max_length=20, blank=True)
    Ensembl_id = models.CharField(max_length=20, blank=True)
    infos = models.TextField(blank=True, verbose_name="Other information")
    #associated_pathology = models.ForeignKey('Pathology',to_field='name',on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)
     
