from django.db import models


# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    field = models.CharField(max_length=100)
    methodology = models.OneToOneField('Methodology', on_delete=models.CASCADE)


class Methodology(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    methodology = models.ForeignKey('Methodology', on_delete=models.CASCADE)
