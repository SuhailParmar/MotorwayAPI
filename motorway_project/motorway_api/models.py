from django.db import models


class MotorwayEvent(models.Model):

    motorway_options = [(6, 6)]
    direction_options = [('n', 'n'), ('s', 's'), ('e', 'e'), ('w', 'w')]
    day_options = [('Mon', 'Mon'), ('Tue', 'Tue'),
                   ('Wed', "Wed"), ('Thu', 'Thu'), ('Fri', 'Fri')]
    year_options = [(2017, 2017), (2018, 2018)]

    event_id = models.IntegerField(primary_key=True)
    motorway = models.IntegerField(choices=motorway_options)
    direction = models.CharField(max_length=1, choices=direction_options)
    junction = models.CharField(max_length=255)  # Temporary
    metadata = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    closest_cities = models.CharField(max_length=255)

    time_timestamp = models.CharField(max_length=255)
    time_day_worded = models.CharField(max_length=3, choices=day_options)
    time_year = models.IntegerField(choices=year_options)
    time_day_numerical = models.IntegerField()
    time_hour = models.IntegerField()
    time_minutes = models.IntegerField()
    time_seconds = models.IntegerField()

    def __str__(self):
        return self.get_event_id

    def get_event_id(self):
        return self.event_id
