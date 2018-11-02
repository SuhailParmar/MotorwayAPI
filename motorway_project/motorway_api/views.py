from rest_framework import generics
from .models import MotorwayEvent
from .serializers import MotorwayEventSerializer

"""
Views are how to get objects from the database
https://www.django-rest-framework.org/api-guide/generic-views/#generic-views
"""


class ListAllEventsView(generics.ListAPIView):
    """
    Return a list of all the MotorwayEvents
    """
    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer
