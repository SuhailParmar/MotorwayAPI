import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from events_helper import Event, ApiClientHelper


@pytest.mark.django_db
class TestEventsPkEndpoint():
    """
    Ensure that the /events/pk endpoint is fully functional
    GET pk and DELETE pk
    """

    e = Event()  # Build generic payload
    client = ApiClientHelper()

    def test_event_doesnt_exist_404_raised(self):
        # Get an event from the db
        # /api/events/105.
        id = 1052482906797428737
        url = reverse('events-retrievedestroy',
                      kwargs={'pk': id})
        response = self.client.get_event(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        response = APIClient().delete(
            reverse("events-retrievedestroy", kwargs={"pk": id}))
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get_specific_event(self):

        # Define the Event ID and build the payload
        id = 1052482906797428737
        self.e.event_id = id
        json_payload = self.e.build_payload()
        self.client.post_event(json_payload)

        # Post a second Event ID and build the payload
        second_id = 9052482906797428738
        self.e.event_id = second_id
        json_payload = self.e.build_payload()
        self.client.post_event(json_payload)

        url = reverse('events-retrievedestroy',
                      kwargs={'pk': 1052482906797428737})
        response = self.client.get_event(url)
        assert response.status_code == status.HTTP_200_OK
        response_data = response.data
        # Ensure the response is one json object (dict) not
        # An array of 2 json objects
        assert isinstance(response_data, dict)
        assert response_data["event_id"] == id

    def test_delete_specific_event(self):
        # Define the Event ID and build the payload
        id = 1052482906797428737
        self.e.event_id = id
        json_payload = self.e.build_payload()
        response = self.client.post_event(json_payload)
        assert response.status_code == status.HTTP_201_CREATED
        # Delete from ID
        response = APIClient().delete(
            reverse("events-retrievedestroy", kwargs={"pk": id}))
        assert response.status_code == status.HTTP_204_NO_CONTENT
