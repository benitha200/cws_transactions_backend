from rest_framework import serializers
from .models import Cws

class CwsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cws
        fields='__all__'
