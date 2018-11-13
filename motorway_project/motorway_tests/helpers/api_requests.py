from django.urls import reverse
from os import getenv
from json import loads, dumps
from requests import post, get, delete


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
        self.all_ep = reverse('events-all')
        self.post_ep = reverse('create-filter')
        self.events_ep = '/api/events/'

    def delete_event(self, id, token):
        """
        Delete from an un-mocked instance of the API
        """
        url = self.base_url + self.events_ep + str(id)
        response = delete(url, headers={'Content-Type': 'application/json',
                                        'Authorization': "Bearer {0}".format(token)})
        return response.status_code

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

    def get_filtered(self, token,  param, return_status=True):
        url = self.base_url + self.events_ep
        response = get(url, headers={'Content-Type': 'application/json',
                                     'Authorization': "Bearer {0}".format(token)},
                       params=param)

        if return_status:
            return response.status_code
        return loads(response.content)

    def get_from_all_endpoint(self, token, return_status=True):
        """
        Get /all un-mocked, requires authentication
        """
        url = self.base_url + self.all_ep
        response = get(url, headers={'Authorization': "Bearer {}".format(
            token), 'Content-Type': 'application/json'})

        if return_status:
            return response.status_code
        return loads(response.content)

    def post_event(self, json_payload, token, return_status=True):
        """
        Post to an un-mocked instance of the API,
        @return_status: return the status code of the post request, or
                        return the contents
        """
        url = self.base_url + self.post_ep
        j = dumps(json_payload)

        request = post(url, data=j, headers={
            'Content-Type': 'application/json',
            'Authorization': "Bearer {0}".format(token)})

        if request.status_code == 400:
            if loads(request.content) ==\
                    {'event_id': ['motorway event with this event id already exists.']}:
                print(
                    "Event {0} already pre-exists :)".format(json_payload['event_id']))
                return 201

        if return_status:
            return request.status_code
        return loads(request.content)
