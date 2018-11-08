import pytest
from helpers.api_requests import APIRequests
from helpers.event import Event


@pytest.mark.django_db
class TestEventsAllEndpoint:
    """
    Ensure that the /events/all endpoint is fully functional
    and protected.
    """
    event_id_1 = 101
    event_id_2 = 102
    client = APIRequests()

    def test_events_all_protected_endpoint(self):
        """
        Using a mocked instance as the api_requests.get_from_all
        Retreives a token to authenticate to the endpoint.
        """
        status_code = self.client.fake_get_all()
        assert status_code == 401

    def test_setup(self):
        self.client.delete_event(1052482906797428737)
        e = Event(event_id=self.event_id_1)
        # Post one event to the db
        json_payload = e.build_payload()
        token = self.client.get_auth_token(scope='write')
        status_code = self.client.post_event(json_payload, token)
        assert status_code == 201

        # Post a second event to the db
        json_payload["event_id"] = self.event_id_2
        status_code = self.client.post_event(json_payload, token)
        assert status_code == 201

    def test_events_all_endpoint(self):
        response = self.client.get_from_all_endpoint()
        assert len(response) == 2
        assert response[0]['event_id'] == self.event_id_1
        assert response[1]['event_id'] == self.event_id_2

    def test_clear_down(self):
        assert self.client.delete_event(self.event_id_1) == 204
        assert self.client.delete_event(self.event_id_2) == 204
