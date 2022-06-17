from django.contrib.auth.models import User, Group
from .models import UserMock
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import UserMock


from rest_framework.decorators import action
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserMock.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        id = self.request.query_params.get('id')
        query = None
        if username is not None:
            query = self.queryset.filter(name=username)
        elif id is not None:
            query = self.queryset.filter(id=id)
        
        return query


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    
