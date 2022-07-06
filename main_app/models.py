from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    sciname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name