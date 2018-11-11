# Motorway API Tests/Development

### Ensure you're working in a virtual_env created in the root directory as so:
```sh
motorway_db
|
env # Your virtual env based on requirements.txt
|
motorway_project/
│
├── motorway_project
├── motorway_api
├── motorway_tests
├── manage.py
├── requirements.txt

```

### The env variables need to be set for database access:

```sh
export POSTGRES_USER="up_to_you"
export POSTGRES_PASSWORD="up_to_you"
export POSTGRES_DB="motorway_db"
# Test fields explained in Register section
# Currently only one is required
export TEST_CLIENT_R_ID="up_to_you"
export TEST_CLIENT_W_ID="up_to_you"
export TEST_CLIENT_R_SECRET="up_to_you"
export TEST_CLIENT_W_SECRET="up_to_you"
```

### Some of the tests require a real instance of the API & DB to test against
```sh
docker-compose up -d motorway_db

# Ensure the db is up to date
python manage.py makemigrations &&
python manage.py migrate

# Wait until db is up
docker-compose up -d motorway_api
```

### Register The Applications

In order to assign tokens to test_applications register 2 apps

```sh
http://localhost:8000/oauth2/applications/register/

- Client Type: Confidential
- Auth Grant Type: Client Credentials
```

Register two applications, one called Read, another with Write.
Assign the id and secret as defined in the environment.

