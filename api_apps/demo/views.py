from django.shortcuts import render
from rest_framework import viewsets
from .models import Bag, Item
from .serializer import BagSerializer, ItemSerializer
# Create your views here.

class BagViewSet(viewsets.ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


