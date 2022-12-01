from django.db import models

# Create your models here.
class Details(models.Model):
    user_name=models.CharField(max_length=20,default='', null=False)
    pswd = models.CharField(max_length=20, default='', null=False)