import sys
from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import FavoriteSerializer, GameSerializer
from .models import Game, Favorite

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('-release_year')
    serializer_class = GameSerializer

class GameListApi(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all()
        option = self.request.query_params.get('option')
        limit = self.request.query_params.get('limit')
        print(limit)
        final_limit = limit if limit else 5
        if option == 'featured':
            return Game.filter_featured(final_limit)
        elif option == 'recent':
            print('josi')
        return queryset


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def create(self, request):
        game = request.data['game']
        user = request.data['user']
        rating = request.data['rating']
        to_save = Favorite.objects.update_or_create(
            game_id=game, user_id=user, defaults={'rating': rating}
        )
        return HttpResponse("Ok")


    def get_queryset(self):
        queryset = Favorite.objects.all()
        user = self.request.query_params.get('user')
        game = self.request.query_params.get('game')

        if user and game:
            return Favorite.objects.filter(user__id=user, game__id=game)
        elif user: 
            return Favorite.objects.filter(user__id=user)
        else: 
            return queryset 

