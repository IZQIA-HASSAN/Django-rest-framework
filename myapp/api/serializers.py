from rest_framework import serializers
from .models import Student

class Stu_serializer(serializers.Serializer):
     name = serializers.CharField(max_length=100)
     roll = serializers.IntegerField()
     city = serializers.CharField(max_length=100)



