from django.db import models

# Create your models here.

class Problem (models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
