from rest_framework import serializers

from models import Part, Place

class PlaceSerializer(serializers.ModelSerializer):
    path = serializers.CharField()
    class Meta:
        model = Place

class PartSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    class Meta:
        model = Part


