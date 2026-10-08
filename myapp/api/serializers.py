from rest_framework import serializers
from .models import Student


# validators 
def start_wit_r(value):
     if value[0].lower() != 'r':
          raise serializers.ValidationError("Name shoud start with r")


class Stu_serializer(serializers.Serializer):
     name = serializers.CharField(max_length=100 , validators=[start_wit_r])
     roll = serializers.IntegerField()
     city = serializers.CharField(max_length=100)

     def create(self , validated_data):
          return Student.objects.create(**validated_data)

     def update(self , instance , validated_data):
          print(instance.name)
          instance.name = validated_data.get('name' ,instance.name)
          print(instance.name)
          instance.roll = validated_data.get('roll' ,instance.name)
          instance.city = validated_data.get('city' ,instance.name)
          instance.save()
          return instance

     # Felld Level validation for roll

     def validate_roll(self , value):
          if value >= 200:
               raise serializers.ValidationError('seat full')

          return value

     #Object level validation

     def validate(self , data):
          nm = data.get('name')
          ct = data.get('city')

          if nm.lower() == 'meerali' and ct.lower() != 'mansehra':
               raise serializers.ValidationError("city must be mansehra")

          return data






