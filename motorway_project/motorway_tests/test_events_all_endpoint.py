import pytest
from events_helper import Event, ApiClientHelper
from rest_framework.test import APIClient
from django.urls import reverse
import json
from os import getenv
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestEventsAllEndpoint:
    """
    Ensure that the /events/all endpoint is fully functional
    """
    e = Event()  # Build generic payload
    json_payload = e.build_payload()
    client = ApiClientHelper()

    def a_test_auth(self):
        assert self.response.status_code == 200
        assert'access_token' in json.loads(self.response.content)

    def test_events_all_endpoint(self):

        self.client.post_event(self.json_payload)

        # Post a second Event ID and build the payload
        second_id = 9052482906797428738
        self.e.event_id = second_id
        json_payload = self.e.build_payload()
        req = self.client.post_event(json_payload)

        response = self.client.get_event(reverse("events-all"))

        response_data = response.data
        assert len(response_data) == 2
        assert response_data[0]['event_id'] == 1052482906797428737
        assert response_data[1]['event_id'] == 9052482906797428738
