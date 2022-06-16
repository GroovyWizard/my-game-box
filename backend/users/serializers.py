from rest_framework import serializers 
from users.models import UserMock
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserMock
        fields = ['id', 'name', 'password']
