from rest_framework import serializers
from .models import Bag, Item

class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'