from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import UpdateAPIView

from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import TokenHasScope, \
    OAuth2Authentication, TokenHasReadWriteScope
from .models import MotorwayEvent
from .serializers import MotorwayEventSerializer
from rest_framework.response import Response
import logging

"""
Views are how to get objects from the database
https://www.django-rest-framework.org/api-guide/generic-views/#generic-views
"""

class RetrieveDestroyEventView(RetrieveDestroyAPIView, UpdateAPIView):
    """ Get and DELETE from id /events/pk """

    permission_classes = [TokenHasReadWriteScope]
    serializer_class = MotorwayEventSerializer
    authentication_classes = [OAuth2Authentication]
    queryset = MotorwayEvent.objects.all()


class CreateFilterView(ListCreateAPIView):
    """ POST (create) and GET (filtered) events at /events"""
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = MotorwayEventSerializer
    authentication_classes = [OAuth2Authentication]

    def get_queryset(self):
        query_params = self.request.query_params
        return MotorwayEvent.objects.filter(
            **query_params.dict())


class ListAllEventsView(ListAPIView):
    """ Return a list of all the MotorwayEvents mapped to /all """
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    queryset = MotorwayEvent.objects.all()
    serializer_class = MotorwayEventSerializer
