from .models import Game, Favorite, Played, Playing
from rest_framework import serializers
from users.serializers import UserSerializer


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'rating', 'description',
                  'publisher', 'release_year', 'banner_img', 'uploaded_image']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        self.fields['game'] = GameSerializer(read_only=True)
        return super(FavoriteSerializer, self).to_representation(instance)



class PlayedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Played
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        self.fields['game'] = GameSerializer(read_only=True)
        return super(PlayedSerializer, self).to_representation(instance)

class PlayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playing
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        self.fields['game'] = GameSerializer(read_only=True)
        return super(PlayingSerializer, self).to_representation(instance)