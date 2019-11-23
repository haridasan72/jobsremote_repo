from django.db import models

# Create your models here.
class hydjob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phoneno = models.IntegerField()

class kerjob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phoneno = models.IntegerField()

class banjob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phoneno = models.IntegerField()

class chejob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phoneno = models.IntegerField()
