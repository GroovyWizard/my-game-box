from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from users.models import UserMock

class Game(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField()
    publisher = models.CharField(max_length=50)
    release_year = models.IntegerField(validators=[MinValueValidator(1970), MaxValueValidator(2100)])
    banner_img = models.TextField()
    uploaded_image = models.ImageField(upload_to = 'uploads/', null=True, blank=True)


    @staticmethod
    def filter_featured(limit):
        return Game.objects.all().order_by('-rating')[:limit]


class Favorite(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user = models.ForeignKey(UserMock, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Playing(models.Model):
    user = models.ForeignKey(UserMock, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Played(models.Model):
    user = models.ForeignKey(UserMock, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
