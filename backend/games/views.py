from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import GameSerializer
from .models import Game

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