from .models import Game
from rest_framework import serializers

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game 
        fields = [ 'id','name', 'rating', 'description', 'publisher', 'release_year', 'banner_img']