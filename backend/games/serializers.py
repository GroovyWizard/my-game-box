from .models import Game, Favorite
from rest_framework import serializers
from users.serializers import UserSerializer


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'rating', 'description',
                  'publisher', 'release_year', 'banner_img']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        self.fields['game'] = GameSerializer(read_only=True)
        return super(FavoriteSerializer, self).to_representation(instance)
