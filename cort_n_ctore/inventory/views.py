from rest_framework import viewsets

from inventory.models import Part, Place
from inventory.serializers import PartSerializer, PlaceSerializer

class PartViewSet(viewsets.ModelViewSet):
    """
    A view set for adding and editing parts in the inventory.
    """
    serializer_class = PartSerializer
    queryset = Part.objects.all()

class PlaceViewSet(viewsets.ModelViewSet):
    """
    A view set for places
    """
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
