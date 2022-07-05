from django.db import models

# Create your models here.
class UserMock(models.Model):
    name = models.CharField(max_length=70, blank=False, unique=True, default='')
    password = models.CharField(max_length=200,blank=False, default='')

