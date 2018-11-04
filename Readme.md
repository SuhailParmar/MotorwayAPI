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


