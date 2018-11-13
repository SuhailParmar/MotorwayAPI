# MotorwayAPI Readme

- I want the API to be able to primarily be the store of Motorway Events
- Each Event will be logged in the database

## Running Tests

Ensure the pytest.ini is in the root of the directory
Ensure you have pytest-django installed (see Readme.md)

```sh
cd motorway_project  # Navigate to the project_dir
pytest -vv  # Run the tests in extra_verbose mode
```

### The API will allow for GET operations

All information regarding motorway events

```bash
/api/events
```

### Todo - Query based on params
```python
#Get events at timestamp
url = "/api/events?timestamp='2018-10-17T08:54:13'"

# Get events at timestamp (lazy)
url = "/api/events?timestamp='2018-10-17'"

# Get events for day
url = "/api/events?day='Wed'"
url = "/api/events?day='10'"
```

### OAuth issues

### AIM

Endpoint          METHOD       Requires Auth?
/events/pk        GET          : Anyone can access
/events/?filter   GET          : Anyone can access
/events/all       GET          : Requires Authorization
/events/pk        DELETE       : Requires Authorization
/events/          POST         : Requires Authorization


https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-2


Able to use oauth in practise but I have issues with my tests failing as the test needs to bypass authentication.

```
    response = client2.post(
        'http://localhost:8000/oauth2/token/',
        {
            'grant_type': 'client_credentials',
            'client_id': getenv('TEST_CLIENT_ID'),
            'client_secret': getenv('TEST_CLIENT_SECRET')
        },
        content_type='application/x-www-form-urlencoded',
    )

``````

### OAuth2

How it works:

Client (app wanting to use API)

Resource Server (API client wants to use)

User (Owner of the API grants permission)

Authorization Server (approve or deny request)

Create a User
read_user  # http://localhost:8000/admin/auth/user/add/
with a username and password

Create/Register the Application
http://localhost:8000/admin/oauth2_provider/application/add/

- Give a name to this app (test_app)
- register a client_id: (test_user)
- register confidential & client_credentials
- get client secret: (test_secret)

Client -> User
(client-credentials pls)

