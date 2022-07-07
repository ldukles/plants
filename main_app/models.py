from django.db import models
from django.urls import reverse

LIGHTS = (
    ('F', 'Full Sun'),
    ('P', 'Partial Sun'),
    ('S', 'Shade')
)

MOISTURES = (
    ('D', 'Dry'),
    ('M', 'Medium'),
    ('W', 'Wet')
)

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    sciname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Conditions(models.Model):
    light = models.CharField(
        max_length=1,
        choices=LIGHTS,
        default=LIGHTS[0][0]
    )
    moisture = models.CharField(
        max_length=1,
        choices=MOISTURES,
        default=MOISTURES[0][0]
    )

        # FOREIGN KEY
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_light_display()} on {self.get_moisture_display()}"
