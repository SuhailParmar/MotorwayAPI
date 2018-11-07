import pytest
from helpers.api_requests import APIRequests
from helpers.event import Event


@pytest.mark.django_db
class TestPostEndpoint():

    client = APIRequests()
    e = Event(event_id=101)
    json_payload = e.build_payload()

    def test_unauthorized_when_post_event(self):
        # If no token present, in this case
        # Using the fake_post_event func.
        status_code = self.client.fake_post_event(self.json_payload)
        assert status_code == 401

    def test_authorized_post_with_token(self):
        # Using the real post endpoint with a valid token
        token = self.client.get_auth_token(scope='Write')
        status_code = self.client.post_event(self.json_payload, token)
        assert status_code == 201
