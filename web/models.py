from __future__ import unicode_literals

from django.db import models

# Create your models here.
class contact(models.Model):
    username = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=50)
     
     
    
class epg_group(models.Model):
    epg_platform = models.CharField(max_length=20)
    epg_name = models.CharField(max_length=20)
    epg_code = models.CharField(max_length=20)
    epg_type = models.CharField(max_length=20)