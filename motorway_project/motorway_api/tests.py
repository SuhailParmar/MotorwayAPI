from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import MotorwayEvent


class ModelTestCase(TestCase):
    """ Testing operations of MotorwayEvent """

    def setUp(self):
        self.client = APIClient()
        # Motorway Tweet Converter
        self.json_payload = {
            "closest_cities": [
                "Stafford (N)",
                "Stoke / Newcastle-u-Lyme"
            ],
            "direction": "n",
            "extra_information": [],
            "id": 1052482906797428736,
            "junction": [
                14,
                15
            ],
            "metadata": "Event Generated by Tweet Miner at 2018-10-20T20:50:12.286910",
            "motorway": 6,
            "reason": "congestion",
            "time_day_numerical": 17,
            "time_day_worded": "Wed",
            "time_hour": 8,
            "time_minutes": 54,
            "time_seconds": 13,
            "time_timestamp": "2018-10-17T08:54:13",
            "time_year": 2018
        }

    """
    def test_add_event_to_db(self):
        pre_add = MotorwayEvent.objects.count()
        assert pre_add == 0
        self.motorway_event.save()  # Add event to db
        post_add = MotorwayEvent.objects.count()
        assert post_add == 1

    def test_remove_event_from_db(self):
        self.motorway_event.delete()  # Delete event to db
        post_del = MotorwayEvent.objects.count()
        assert post_del == 0
    """

    def test_post_event_successful(self):

        post_data = {'data': self.json_payload}

        response = self.client.post(
            reverse('create'),
            post_data,
            format="json"
        )

        assert response.status_code == status.HTTP_201_CREATED