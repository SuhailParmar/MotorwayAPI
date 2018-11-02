from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from .models import MotorwayEvent
from .serializers import MotorwayEventSerializer

"""
Views are how to get objects from the database
https://www.django-rest-framework.org/api-guide/generic-views/#generic-views
"""


class ListAllEventsView(ListAPIView):
    """
    Return a list of all the MotorwayEvents
    """
    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer


class CreateEventView(CreateAPIView):
    """
    Ability to Create n MotorwayEvents
    """
    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer
