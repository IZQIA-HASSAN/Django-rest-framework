from rest_framework import serializers

from .models import Student



class studentserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id' , 'url' , 'name' , 'roll' , 'city']