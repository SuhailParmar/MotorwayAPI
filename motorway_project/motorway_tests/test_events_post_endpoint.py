import pytest
from helpers.api_requests import APIRequests
from helpers.event import Event


@pytest.mark.django_db
class TestPostEndpoint():
    """
    Testing the ability to POST to a
    protected /api/events/ endpoint
    """
    client = APIRequests()
    token = client.get_auth_token(scope='write')
    event_id_1 = 101
    e = Event(event_id=event_id_1)
    json_payload = e.build_payload()

    def test_unauthorized_to_post_without_token(self):
        # If no token present, in this case
        # Using the fake_post_event func.
        status_code = self.client.fake_post_event(self.json_payload)
        assert status_code == 401

    def test_authorized_post_with_token(self):
        # Using the real post endpoint with a valid token
        status_code = self.client.post_event(self.json_payload, self.token)
        assert status_code == 201
        # Clear event from db
        token = self.client.get_auth_token(scope='delete')
        assert self.client.delete_event(self.event_id_1, token) == 204

    def test_event_contains_extra_info_field_after_post(self):
        # The json_payload doesn't contain an extra_information field
        # As it's an optional field.
        # We need to ensure it is present and blank after post
        assert self.json_payload.get('extra_information') is None
        # Request the client returns data not the status_code
        response_data = self.client.post_event(
            self.json_payload, self.token, response='data')
        assert response_data["extra_information"] == ""

    def test_clear_down(self):
        token = self.client.get_auth_token(scope='delete')
        assert self.client.delete_event(self.event_id_1, token) == 204
