from django.db import models
from django.contrib.postgres.fields import ArrayField


class MotorwayEventManager(models.Manager):
    def create_event(self,
                     event_id,
                     motorway,
                     direction,
                     junction,
                     metadata,
                     reason,
                     closest_cities,
                     time_timestamp,
                     time_day_worded,
                     time_year,
                     time_day,
                     time_hour,
                     time_minutes,
                     time_seconds):

        event = self.create(
            event_id, motorway, direction, junction, metadata, reason,
            closest_cities, time_timestamp, time_day_worded, time_year,
            time_day, time_hour, time_minutes, time_seconds,)

        return event


class MotorwayEvent(models.Model):

    motorway_options = [(1, 1), (6, 6), (25, 25), (40, 40)]
    direction_options = [('n', 'n'), ('s', 's'), ('e', 'e'),
                         ('w', 'w'), ('c', 'c'), ('ac', 'ac')]
    day_options = [('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', "Wed"),
                   ('Thu', 'Thu'), ('Fri', 'Fri'), ('Sat', 'Sat'),
                   ('Sun', 'Sun')]

    year_options = [("2017", "2017"), ("2018", "2018"), ("2019", "2019")]

    event_id = models.BigIntegerField(primary_key=True)

    junction = ArrayField(
        models.IntegerField(),
        size=3
    )

    closest_cities = ArrayField(
        models.CharField(max_length=255)
    )

    extra_information = ArrayField(
        models.CharField(blank=True, max_length=255)
    )

    motorway = models.CharField(choices=motorway_options, max_length=4)
    direction = models.CharField(max_length=1, choices=direction_options)
    metadata = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    time_timestamp = models.DateTimeField()
    time_day_worded = models.CharField(max_length=3, choices=day_options)
    time_year = models.CharField(max_length=4, choices=year_options)
    time_day = models.CharField(max_length=10)
    time_hour = models.CharField(max_length=3)
    time_minutes = models.CharField(max_length=3)
    time_seconds = models.CharField(max_length=3)

    objects = MotorwayEventManager()

    def __str__(self):
        return self.get_event_id

    def get_event_id(self):
        return self.event_id
