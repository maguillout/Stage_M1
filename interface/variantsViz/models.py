from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Table(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sample_id = models.CharField(max_length=200)
    path_file = models.CharField(max_length=200)
    real_path_file = models.FilePathField(path='/home/maelle/Bureau/Stage/Data')
    #text = models.TextField()
    tab = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sample_id

    def importation(self):
        self.tab=pd.read_csv(self.path_file, sep =';')

class Job(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sample_id = models.CharField(max_length=200)
    real_path_file = models.FilePathField(path='/home/maelle/Bureau/Stage/Data')
    #info = models.TextField(default=None)
    start_date = models.DateTimeField(default=timezone.now)
    running = models.BooleanField(default=True)    

    def __str__(self):
        return self.sample_id

from django.contrib.auth.models import User

