from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

BLOOMS = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

class Condition(models.Model):
    sun = models.CharField(max_length=15)
    moisture = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.moisture} {self.sun}'

    def get_absolute_url(self):
        return reverse('conditions_detail', kwargs={'pk': self.id})

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    sciname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)
    conditions = models.ManyToManyField(Condition)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Bloom(models.Model):
    date = models.DateField('')
    bloom = models.CharField(
        max_length=1,
        choices=BLOOMS,
        default=BLOOMS[0][0]
    )
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_bloom_display()} on {self.date}"

    class Meta:
     ordering = ['-date']

        # FOREIGN KEY
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_bloom_display()} on {self.date}"



class Photo(models.Model):
    url = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for plant_id: {self.plant_id} @{self.url}"