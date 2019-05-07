from django.db import models

# Create your models here
class Box(models.model):
    name = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
