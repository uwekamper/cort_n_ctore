from rest_framework import serializers

from models import Part, Place

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place