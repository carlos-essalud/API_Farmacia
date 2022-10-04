from django.db import models

# Create your models here.

class Personal(models.Model):
    centro=models.CharField(max_length=30)