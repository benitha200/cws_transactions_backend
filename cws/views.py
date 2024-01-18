from django.shortcuts import render
from rest_framework import generics,permissions
from cws.models import Cws
from .serializers import CwsSerializer

# Create your views here.
class CwsCreateView(generics.CreateAPIView):
    queryset=Cws.objects.all()
    serializer_class=CwsSerializer
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=['post']


class CwsListView(generics.ListAPIView):
    queryset=Cws.objects.all()
    serializer_class=CwsSerializer
    http_method_names=['get']


