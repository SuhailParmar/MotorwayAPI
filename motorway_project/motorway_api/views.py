from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import ListCreateAPIView
from .models import MotorwayEvent
from .serializers import MotorwayEventSerializer

"""
Views are how to get objects from the database
https://www.django-rest-framework.org/api-guide/generic-views/#generic-views
"""


class RetrieveDestroyEventView(RetrieveDestroyAPIView):
    """ Get and DELETE from id /events/pk """

    # The DELETE an event needs ADMIN/AUTH permissions

    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer


class CreateFilterView(ListCreateAPIView):
    """ POST (create) and GET (filtered) events at /events"""
    serializer_class = MotorwayEventSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        # Need to unpack query_params as multiple kwargs: id: 0, info: hello
        return MotorwayEvent.objects.filter(**query_params)


class ListAllEventsView(ListAPIView):
    """ Return a list of all the MotorwayEvents mapped to /all """
    # Testing Permissions to view all
    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer
