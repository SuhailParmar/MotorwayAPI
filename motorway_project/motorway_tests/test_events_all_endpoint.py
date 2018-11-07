import pytest
from helpers.api_requests import APIRequests
from helpers.event import Event


@pytest.mark.django_db
class TestEventsAllEndpoint:
    """
    Ensure that the /events/all endpoint is fully functional
    """
    event_id_1 = 101
    event_id_2 = 102
    client = APIRequests()

    def test_events_all_endpoint(self):
        e = Event(event_id=self.event_id_1)  # Build generic payload
        json_payload = e.build_payload()

        status_code = self.client.post_event(json_payload)
        assert status_code == 201

        # Post a second Event ID and build the payload
        json_payload["event_id"] = self.event_id_2
        status_code = self.client.post_event(json_payload)
        assert status_code == 201

        response = self.client.get_from_all_endpoint()
        assert len(response) == 2
        assert response[0]['event_id'] == self.event_id_1
        assert response[1]['event_id'] == self.event_id_2

    def test_clear_down(self):
        assert self.client.delete_event(self.event_id_1) == 204
        assert self.client.delete_event(self.event_id_2) == 204
