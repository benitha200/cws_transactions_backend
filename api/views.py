from django.shortcuts import render
from rest_framework import generics,permissions
from farmers.models import Farmer
from .serializers import FarmerSerializer


# Create your views here.

class FarmerCreateView(generics.CreateAPIView):
    queryset=Farmer.objects.all()
    serializer_class=FarmerSerializer
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=['post']


class FarmerListView(generics.ListAPIView):
    queryset=Farmer.objects.all()
    serializer_class=FarmerSerializer
    http_method_names=['get']

    