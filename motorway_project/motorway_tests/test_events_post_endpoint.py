import pytest
from helpers.api_requests import APIRequests
from helpers.event import Event
from json import loads


@pytest.mark.django_db
class TestPostEndpoint():
    """
    Testing the ability to POST to a
    protected /api/events/ endpoint
    """
    client = APIRequests()
    token = client.get_auth_token(scope='write')
    event_id_1 = 109
    e = Event(event_id=event_id_1)
    json_payload = e.build_payload()

    def test_unauthorized_to_post_without_token(self):
        # If no token present, in this case
        r = self.client.post_event(self.json_payload, token=None)
        assert r.status_code == 401

    def test_authorized_post_with_token(self):
        # Using the real post endpoint with a valid token
        r = self.client.post_event(self.json_payload, self.token)
        assert r.status_code == 201
        # Clear event from db
        token = self.client.get_auth_token(scope='delete')
        status_code = self.client.delete_event(self.event_id_1, token)
        assert status_code == 204

    def test_event_contains_extra_info_field_after_post(self):
        # Request the client returns data not the status_code
        r = self.client.post_event(
            self.json_payload, self.token, False)

        d = loads(r.content)
        assert (d["extra_information"] == [])

    def test_clear_down(self):
        token = self.client.get_auth_token(scope='delete')
        status_code = self.client.delete_event(self.event_id_1, token)
        assert status_code == 204
