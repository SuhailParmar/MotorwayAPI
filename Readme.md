# MotorwayAPI Readme

- I want the API to be able to primarily be the store of Motorway Events
- Each Event will be logged in the database


### The API Will allow for the converter and the enricher to POST to the endpoint
```python
url = "/api/events/" # Post With payload, CT = application/json
```

It will require authentication to POST to this url.
PATCH is not a


### The API will allow for GET operations

All information regarding motorway events

```bash
/api/events
```

Example GET Queries
```python
#Get events at timestamp
url = "/api/events?timestamp='2018-10-17T08:54:13'"

# Get events at timestamp (lazy)
url = "/api/events?timestamp='2018-10-17'"

# Get events for day
url = "/api/events?day='Wed'"
url = "/api/events?day='10'"

all_optional_params = [
    closest_cities,
    direction,
    extra_information,
    id,
    junction,
    metadata,
    motorway,
    reason congestion,
    time_day_numerical,
    time_day_worded,
    time_hour,
    time_minutes,
    time_seconds,
    time_timestamp,
    time_year
]

```


