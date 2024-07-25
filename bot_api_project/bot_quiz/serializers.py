from .models import Advise
from rest_framework import serializers
from datetime import datetime

class DateTimeSerializer(serializers.Serializer):
    current_datetime = serializers.DateTimeField()
    
class AdviseSerializer(serializers.ModelSerializer):
    
    """
    Serializer for the Advise model.

    Converts Advise model instances to JSON format and validates input data.
    """
    
    class Meta:
        model = Advise
        fields = ['text']