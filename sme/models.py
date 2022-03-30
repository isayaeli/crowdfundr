from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Project(models.Model):
    title =  models.CharField(max_length=100)
    project_duration = models.CharField(max_length=100)
    beneficiaries = models.TextField()
    target_area = models.TextField()
    project_overview = models.TextField()
    proposal = models.FileField(upload_to='proposals', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True,blank=True)

    def __str__(self):
        return self.title