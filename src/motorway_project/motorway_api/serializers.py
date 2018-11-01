from rest_framework import serializers
from .models import MotorwayEvent

"""
Serializers == Converters
- They convert data into python datatypes
- Convert python datatypes to complex data
"""


class MotorwayEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorwayEvent
        fields = ("id")
