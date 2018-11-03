from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView

from .models import MotorwayEvent
from .serializers import MotorwayEventSerializer

"""
Views are how to get objects from the database
https://www.django-rest-framework.org/api-guide/generic-views/#generic-views
"""


class ListAllEventsView(ListAPIView):
    """
    Return a list of all the MotorwayEvents mapped to /all
    """
    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer


class CreateEventView(CreateAPIView):
    """
    Ability to POST n MotorwayEvents at /events
    """
    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer
