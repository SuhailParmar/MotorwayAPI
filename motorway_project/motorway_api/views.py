from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import ListCreateAPIView
from oauth2_provider.contrib.rest_framework import TokenMatchesOASRequirements
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication, TokenHasReadWriteScope
from oauth2_provider.views.generic import ReadWriteScopedResourceView
from .models import MotorwayEvent
from .serializers import MotorwayEventSerializer
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.decorators import protected_resource
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
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = MotorwayEventSerializer
    authentication_classes = [OAuth2Authentication]

    def get_queryset(self):
        query_params = self.request.query_params
        # Need to unpack query_params as multiple kwargs: id: 0, info: hello
        return MotorwayEvent.objects.filter(**query_params)


class ListAllEventsView(ListAPIView):
    """ Return a list of all the MotorwayEvents mapped to /all """
    #permission_classes = [TokenHasScope]
    #required_scopes = ['read']
    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer
