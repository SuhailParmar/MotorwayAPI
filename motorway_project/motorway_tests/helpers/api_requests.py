from django.urls import reverse
from os import getenv
from json import loads, dumps
from requests import post, get, delete
from rest_framework.test import APIRequestFactory, APIClient


class APIRequests():
    """
    Custom Library to help with testing
    - Issues with retrieving an OAuth token from the APIClient
      lib, so for protected endpoints use the real instance and
      clear up events after
    """

    def __init__(self):
        self.base_url = 'http://localhost:8000'
        self.token_ep = '/oauth2/token/'
        self.all_ep = reverse('events-all') # Protected EP
        self.post_ep = reverse('create-filter')
        self.events_ep = '/api/events/'

    def get_auth_token(self):
        """
        Authenticate to unmocked API using test credentials
        """
        url = self.base_url + self.token_ep
        client_id = getenv('TEST_CLIENT_ID', 'test_id')
        client_secret = getenv('TEST_CLIENT_SECRET', 'test_secret')
        grant_type = "client_credentials"

        request = post(url,  # Request Auth token
                       data="grant_type={0}&client_id={1}&client_secret={2}"
                       .format(grant_type, client_id, client_secret),
                       headers={'Content-Type': 'application/x-www-form-urlencoded'})

        if request.status_code != 200:
            raise ValueError

        content = loads(request.content)
        return content['access_token']

    def fake_post_event(self, payload):
        client = APIClient()
        req = client.post(self.post_ep, data=payload, format='json')
        return req.status_code

    def fake_get_event(self):
        client = APIRequestFactory()
        req = client.get(self.all_ep)
        force_authenticate(req, user=None, token=self.get_fake_auth())
        return req

    def post_event(self, json_payload):
        """
        Post to an un-mocked instance of the API
        """
        url = self.base_url + self.post_ep
        j = dumps(json_payload)
        request = post(url, data=j, headers={'Content-Type': 'application/json'})

        if loads(request.content) == {'event_id': ['motorway event with this event id already exists.']}:
            print("Event {0} already pre-exists :)".format(json_payload['event_id']))
            return 201

        return request.status_code

    def delete_event(self, id):
        """
        Delete to an un-mocked instance of the API
        """
        url = self.base_url + self.events_ep + str(id)
        response = delete(url, headers={'Content-Type': 'application/json'})
        return response.status_code

    def get_from_all_endpoint(self):
        """
        Get /all un-mocked, requires authentication
        """
        url = self.base_url + self.all_ep
        token = self.get_auth_token()
        response = get(url, headers={'Authorization': "Bearer {}".format(token), 'Content-Type': 'application/json'})

        return loads(response.content)
