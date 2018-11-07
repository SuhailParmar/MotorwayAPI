import pytest
from motorway_tests.helpers.api_requests import APIRequests


@pytest.mark.django_db
class TestClearDownDB():

    client = APIRequests()

    def test_clear_down(self):
        """ Not an official test but an easy
        way to clear down the live database
        pytest -vx test_clear_db.py
        """
        response = self.client.get_from_all_endpoint()
        for event in response:
            id = event["event_id"]
            assert self.client.delete_event(id) == 204
            print("Deleted event {0}".format(id))
