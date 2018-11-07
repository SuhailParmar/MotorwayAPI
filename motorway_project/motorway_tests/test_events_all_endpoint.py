import pytest
from events_helper import Event, APIRequests
from rest_framework.test import APIClient
from django.urls import reverse
import requests

@pytest.mark.django_db
class TestEventsAllEndpoint:
    """
    Ensure that the /events/all endpoint is fully functional
    """
    e = Event()  # Build generic payload
    json_payload = e.build_payload()
    client = APIRequests()

    def test_events_all_endpoint(self):

        status_code = self.client.post_event(self.json_payload)
        assert status_code == 201

        # Post a second Event ID and build the payload
        second_id = 9052482906797428738
        self.e.event_id = second_id
        json_payload = self.e.build_payload()
        status_code = self.client.post_event(json_payload)

        assert status_code == 201

        response = self.client.get_all_ep()

        assert len(response) == 2
        assert response[0]['event_id'] == 1052482906797428737
        assert response[1]['event_id'] == 9052482906797428738
