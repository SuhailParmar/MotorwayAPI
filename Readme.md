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

### Available queries
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
/events/pk        GET          : READ access
/events/?filter   GET          : READ access
/events/all       GET          : Requires Authorization
/events/pk        DELETE       : Requires Authorization
/events/          POST         : Requires Authorization


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

## We will potentially read from rabbit / allow for a post

Potentially use celery for this functionality, celery will be perfoming the background task of binding to the rabbit queue listening for events and writing them to the db.

TO avoid this uneccesary level of complexity, the *tweet converter* will be reponsible for posting the event to the API. But if testing reveals slow down on the POST endpoint then we shall look into this.