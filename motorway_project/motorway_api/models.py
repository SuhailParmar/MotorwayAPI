from django.db import models


class MotorwayEvent(models.Model):
    event_id = models.IntegerField(primary_key=True)
    motorway = models.IntegerField()
    direction = models.CharField(max_length=1)
    metadata = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=255)
    junctions = models.CharField(max_length=255)  # Temporary
    closest_cities = models.CharField(max_length=255)
    time_day_worded = models.CharField(max_length=3)
    time_day_numerical = models.IntegerField()
    time_hour = models.IntegerField()
    time_minutes = models.IntegerField()
    time_seconds = models.IntegerField()
    time_year = models.IntegerField()

    def __str__(self):
        return self.get_event_id

    def get_event_id(self):
        return self.event_id
