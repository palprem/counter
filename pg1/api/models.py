from django.db import models

class DATA(models.Model):
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=100)
    
