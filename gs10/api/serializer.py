from rest_framework import serializers
from .models import Singer , Song

class songserializer(serializers.ModelSerializer):
    class Meta : 
        model = Song
        fields = ['id' , 'title' , 'singer' , 'duration' ]

class singerserializer
