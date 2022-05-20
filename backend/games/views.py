from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GameSerializer
from .models import Game
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('-release_year')
    serializer_class = GameSerializer
    
