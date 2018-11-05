import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from events_helper import Event, ApiClientHelper


@pytest.mark.django_db
class TestEventsCreateFilterEndpoint():
    """
    Ensure that the /events/ endpoint is fully functional
    GET: w/ filters
    POST: w/ params
    Django ensures all of the models fields are present in POST
    So no need to test the framework. E.g test_return_400
    """

    e = Event()
    json_payload = e.build_payload()  # Build generic payload
    client = ApiClientHelper()

    def test_post_event(self):
        # We dont care about the payload contents here
        response = self.client.post_event(self.json_payload)
        assert response.status_code == status.HTTP_201_CREATED

    def test_able_to_filter_by_field(self):
        # Post generic json_payload
        response = self.client.post_event(self.json_payload)
        assert response.status_code == status.HTTP_201_CREATED

        # Create a new event (id and junction)
        self.json_payload['event_id'] = 1052482906797428711
        self.json_payload['junction'] = [5]
        # Post second json_payload
        self.client.post_event(self.json_payload)
        assert response.status_code == status.HTTP_201_CREATED

        # Create a new event (id and Same junction as prev)
        self.json_payload['event_id'] = 1052482906797428712
        self.json_payload['junction'] = [5]
        # Post second json_payload
        self.client.post_event(self.json_payload)
        assert response.status_code == status.HTTP_201_CREATED

        # Get with query params, should be two events
        response = APIClient().get(
            reverse("create-filter"), {'junction': [5]})

        assert len(response.data) == 2
        e1, e2 = response.data[0], response.data[1]
        assert e1["junction"] == [5]
        assert e2["junction"] == [5]

        assert e1["event_id"] == 1052482906797428711
        assert e2["event_id"] == 1052482906797428712

    def test_event_contains_extra_info_field_after_post(self):
        # The json_payload doesn't contain an extra_information field
        # As it's an optional field.
        assert self.json_payload.get('extra_information') is None
        # We need to ensure it is present and blank after post
        response = self.client.post_event(self.json_payload)
        assert response.status_code == status.HTTP_201_CREATED
        response_data = response.data
        assert response_data["extra_information"] == ""

    def test_second_create_event_raises_400(self):
        # We dont care about the payload contents here
        # DB wipes after every test/function so post twice here
        response = self.client.post_event(self.json_payload)
        assert response.status_code == status.HTTP_201_CREATED
        response = self.client.post_event(self.json_payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


