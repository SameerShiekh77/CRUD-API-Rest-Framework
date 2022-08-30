import imp
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    rollNo = serializers.IntegerField()


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance


# Field value validation
    def validate_rollNo(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat full")
        return value


# object level validations
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'sameer' and city.lower() != 'karachi':
            raise serializers.ValidationError("City must be Karachi")
        return data