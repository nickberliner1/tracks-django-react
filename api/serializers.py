from rest_framework import serializers
from .models import ShipmentsData

class ShipmentsDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShipmentsData
        fields = ('type_of_goods', 'weight', 'start_time', 'end_time')