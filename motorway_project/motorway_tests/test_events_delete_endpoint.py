import pytest
from helpers.api_requests import APIRequests
from helpers.event import Event


@pytest.mark.django_db
class TestDeleteEndpoint():
    """
    Testing the ability to POST to a
    protected /api/events/ endpoint
    """

    event_id_1 = 100
    event_id_2 = 200
    client = APIRequests()

    def test_unauthorized_to_delete(self):
        # Deleting without a token
        status_code = self.client.delete_event(self.event_id_1)
        assert status_code == 401

    def test_setup(self):
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

    def test_clear_down(self):
        assert self.client.delete_event(self.event_id_1) == 204
        assert self.client.delete_event(self.event_id_2) == 204