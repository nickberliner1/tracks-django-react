from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ShipmentsDataSerializer
from .models import ShipmentsData


class ShipmentsDataViewSet(viewsets.ModelViewSet):
    queryset = ShipmentsData.objects.all().order_by('id')
    serializer_class = ShipmentsDataSerializer