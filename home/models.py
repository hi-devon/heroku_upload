from django.db import models
from django import forms

# Create your models here.
class Board(models.Model):
    num = models.IntegerField(null=True)
    gubun = models.CharField(null=True, max_length=15)
    reg_date = models.DateField(null=True)
    title = models.CharField(null=True, max_length=100)
    content = models.TextField(null=True)

class Contact(models.Model):
    customer_name = models.CharField(null=True, max_length=15)
    customer_email = models.CharField(null=True, max_length=20)
    title = models.CharField(null=True, max_length=50)
    content = models.TextField(null=True)
    reg_date = models.DateField(null=True)
    
class SettingsInfo(models.Model):
    itemkey = models.CharField(max_length=30)
    itemval = models.CharField(max_length=128)