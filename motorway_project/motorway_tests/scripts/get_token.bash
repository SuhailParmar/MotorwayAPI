
#!/bin/bash

curl -X POST -i -H "Content-Type: application/x-www-form-urlencoded"\
 --data 'grant_type=client_credentials&client_id=test_id&client_secret=test_secret'\
    http://localhost:8000/oauth2/token/

