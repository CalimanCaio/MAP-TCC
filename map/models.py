from django.db import models


class Methodology(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    methodology = models.ForeignKey('Methodology', on_delete=models.CASCADE)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    activities = models.ManyToManyField(Activity)
