from rest_framework import serializers

from .models import Song , Singer




# class studentserializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id' , 'url' , 'name' , 'roll' , 'city']

class Songserializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id' , 'title' , 'singer' , 'duration']


class SingerSerializer(serializers.ModelSerializer):
    sungby = Songserializer(source='song_set',many=True , read_only = True)
    class Meta:
        model = Singer
        fields = ['id' , 'name' , 'gender' , 'sungby']
