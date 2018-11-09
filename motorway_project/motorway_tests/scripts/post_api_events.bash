#!/bin/bash

curl -X POST -i -H "Content-Type: application/json"\
 --data '{"event_id":105,"junction":[1,2],"closest_cities":["test"],"extra_information":"test","motorway":6,"direction":"n","metadata":"test","reason":"test","time_timestamp":"2018-11-06T17:37:06","time_day_worded":"Mon","time_year":2018,"time_day_numerical":1,"time_hour":1,"time_minutes":1,"time_seconds":1}'\
    http://localhost:8000/api/events/

