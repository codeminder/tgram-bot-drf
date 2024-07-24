from .models import Advise
from rest_framework import serializers
from datetime import datetime

class DateTimeSerializer(serializers.Serializer):
    current_datetime = serializers.DateTimeField()
    
class AdviseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advise
        fields = ['text']