import pytest
from helpers.api_requests import APIRequests
from helpers.event import Event


@pytest.mark.django_db
class TestFilterEndpoint():
    """
    Ability to filter events on the protected
    GET /events/?<params> endpoint
    """
    client = APIRequests()
    event_id_1, event_id_2 = 104, 105
    junction_1, junction_2 = [5], [4]

    e = Event(event_id=event_id_1, junction=junction_1)

    def test_setup(self):
        """
        Need >2 elements in the db to be able to test filter
        """
        json_payload = self.e.build_payload()
        token = self.client.get_auth_token(scope='write')
        r = self.client.post_event(json_payload, token)
        assert r.status_code == 201

        json_payload["event_id"] = self.event_id_2
        json_payload["junction"] = self.junction_2

        r = self.client.post_event(json_payload, token)
        assert r.status_code == 201

    def test_able_to_filter_by_field(self):
        token = self.client.get_auth_token(scope='read')
        response = self.client.get_filtered(token, "?junction={5}", False)

        assert len(response) == 1
        # Should only filter one event_id_one
        e1 = response[0]
        assert e1["junction"] == [5]
        assert e1["event_id"] == self.event_id_1

    def test_clear_up(self):
        token = self.client.get_auth_token(scope='delete')
        assert self.client.delete_event(self.event_id_1, token) == 204
        assert self.client.delete_event(self.event_id_2, token) == 204
