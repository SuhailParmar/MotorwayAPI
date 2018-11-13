import pytest
from motorway_tests.helpers.api_requests import APIRequests


@pytest.mark.django_db
class TestClearDownDB():

    client = APIRequests()

    def test_clear_down(self):
        """
        Not an official test but an easy
        way to clear down the live database
        pytest -vx test_clear_db.py
        """
        token = self.client.get_auth_token(scope='delete')
        response = self.client.get_from_all_endpoint(token, False)
        for event in response:
            id = event["event_id"]
            print("Deleting event {0}".format(id))
            assert self.client.delete_event(id, token) == 204
