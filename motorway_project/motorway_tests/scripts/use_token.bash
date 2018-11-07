#!/bin/bash

curl -H "Authorization: Bearer ${1}" -X GET -i http://localhost:8000/api/events/all/

