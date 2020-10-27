from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#models.ForeignKey -> lien vers un autre modèle




class Job(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sample_id = models.CharField(max_length=200)
    real_path_file = models.FilePathField(path='/home/maelle/Bureau/Stage/Data')
    #info = models.TextField(default=None)
    start_date = models.DateTimeField(default=timezone.now)
    running = models.BooleanField(default=True)    

    def __str__(self):
        return self.sample_id


class Pathology(models.Model):  #implementation of the object "pathology"
    #attributes required to add a new pathology
    name = models.CharField(max_length=200)
    infos = models.TextField(blank=True, verbose_name="Other information")
    #associated_gene_OMIM = models.CharField(max_length=200, blank = True)
    associated_genes = models.ManyToManyField('Gene', blank=True)
    #on_delete defines consequences of suppression of the gene, with models.SET_NULL the gene field will be empty  
    initialisation_date = models.DateTimeField(default=timezone.now, editable = False)

    class Meta:
        #definition of the plural name (by default, adds a 's')
        verbose_name_plural = "Pathologies"  

    def __str__(self):
        #prints the pathology (its name)
        return (self.name)


class Gene(models.Model): 
    #attributes required to add a new gene to the database
    name = models.CharField(default="",max_length=200, blank=True)
    MIM_number = models.CharField(max_length=20, blank=True)
    Ensembl_id = models.CharField(max_length=20, blank=True)
    infos = models.TextField(blank=True, verbose_name="Other information")
    associated_pathologies = models.ManyToManyField('Pathology', blank=True)
    initialisation_date = models.DateTimeField(default=timezone.now, editable = False)


    def __str__(self):
        return (self.name)

class Variant(models.Model): 
    rs_id = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=20, blank=True)
    gene = models.ForeignKey('Gene', on_delete=models.CASCADE, blank=True, default="")
    ACMG_diagnostic =  models.CharField(max_length=20, blank=True)
    manual_diagnostic =  models.CharField(max_length=20, blank=True)
    AAchange = models.CharField(max_length=20, blank=True)
    infos = models.TextField(blank=True, verbose_name="Other information")
    clinvar_link = models.CharField(max_length=200, blank=True)
    orphadata_link = models.CharField(max_length=200, blank=True)
    CADD_score = models.CharField(max_length=200, blank=True)
    Polyphen_score = models.CharField(max_length=200, blank=True)
    MutationTaster_score = models.CharField(max_length=200, blank=True)
    associated_pathologies = models.ManyToManyField('Pathology', blank=True)
    initialisation_date = models.DateTimeField(default=timezone.now, editable = False)

    def __str__(self):
        return (self.name)

    def OMIM_link():
        return (f"https://omim.org/entry/{self.associated_gene_OMIM}")


class Patient(models.Model):
    identifiant = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=[(' ','Unknown'),('M','Male'),('F','Female')])
    birth_date = models.DateField()
    age = models.SmallIntegerField()
    age_of_unset = models.SmallIntegerField(blank=True)
    infos = models.TextField(blank=True, verbose_name="Other information",)
    pathology = models.ForeignKey('Pathology', on_delete=models.CASCADE, blank=True, default="")
    initialisation_date = models.DateTimeField(default=timezone.now, editable = False)
    def __str__(self):
        return (self.identifiant)
    

