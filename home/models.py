from django.db import models

# Create your models here.
class Board(models.Model):
    num = models.IntegerField(null=True)
    gubun = models.CharField(null=True, max_length=15)
    reg_date = models.DateField(null=True)
    title = models.CharField(null=True, max_length=100)
    content = models.TextField(null=True)
