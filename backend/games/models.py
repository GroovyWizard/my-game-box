from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Game(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField()
    publisher = models.CharField(max_length=50)
    release_year = models.IntegerField(validators=[MinValueValidator(1970), MaxValueValidator(2100)])
    banner_img = models.TextField()