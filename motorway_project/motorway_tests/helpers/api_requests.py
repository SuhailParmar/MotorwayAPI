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
        self.all_ep = reverse('events-all')  # Protected EP
        self.post_ep = reverse('create-filter')
        self.events_ep = '/api/events/'

    def get_auth_token(self, scope):
        """
        Authenticate to unmocked API using test credentials
        Pre-Req: Ensure 2 apps are registered: Read and Write
        """
        url = self.base_url + self.token_ep
        grant_type = "client_credentials"

        client_id = getenv('TEST_CLIENT_R_ID', 'test_r_id')
        client_secret = getenv('TEST_CLIENT_R_SECRET', 'test_r_secret')

        request = post(url,  # Request Auth token
                       data="grant_type={0}&client_id={1}&client_secret={2}"
                       .format(grant_type, client_id, client_secret),
                       headers={'Content-Type': 'application/x-www-form-urlencoded'})

        if request.status_code != 200:
            print(request.status_code)
            print(request.content)
            raise ValueError

        content = loads(request.content)
        return content['access_token']

    def fake_post_event(self, payload):
        client = APIClient()
        req = client.post(self.post_ep, data=payload, format='json')
        return req.status_code

    def post_event(self, json_payload, token=None, response=None):
        """
        Post to an un-mocked instance of the API
        """
        url = self.base_url + self.post_ep
        j = dumps(json_payload)

        if token:
            request = post(url, data=j, headers={
                           'Content-Type': 'application/json',
                           'Authorization': "Bearer {0}".format(token)})
        else:
            request = post(url, data=j, headers={
                           'Content-Type': 'application/json'})

        if request.status_code == 400:
            if loads(request.content) ==\
                    {'event_id': ['motorway event with this event id already exists.']}:
                print(
                    "Event {0} already pre-exists :)".format(json_payload['event_id']))
                return 201

        if response is not None:
            data = loads(request.content)
            return data

        return request.status_code

    def get_event(self, id):
        """
        Get from an un-mocked instance of the API
        """
        url = self.base_url + self.events_ep + str(id)
        response = get(url, headers={'Content-Type': 'application/json'})
        return response.status_code

    def get_filtered(self, token,  param={"junction": [5]}):
        url = self.base_url + self.events_ep
        response = get(url, headers={'Content-Type': 'application/json',
                                     'Authorization': "Bearer {0}".format(token)},
                       params=param)

        if response.status_code != 200:
            print(response.status_code, response.content)
            raise ValueError

        json_response = loads(response.content)
        return json_response

    def fake_filter_event(self, param={"junction": [5]}):
        client = APIClient()
        url = self.base_url + self.events_ep
        req = client.get(url, data=param, format='json')
        return req.status_code

    def delete_event(self, id):
        """
        Delete from an un-mocked instance of the API
        """
        url = self.base_url + self.events_ep + str(id)
        response = delete(url, headers={'Content-Type': 'application/json'})
        return response.status_code

    def get_from_all_endpoint(self):
        """
        Get /all un-mocked, requires authentication
        """
        url = self.base_url + self.all_ep
        token = self.get_auth_token(scope='read')
        response = get(url, headers={'Authorization': "Bearer {}".format(
            token), 'Content-Type': 'application/json'})

        return loads(response.content)

    def fake_get_all(self):
        url = self.base_url + self.all_ep
        client = APIClient()
        req = client.get(self.post_ep, format='json')
        return req.status_code
