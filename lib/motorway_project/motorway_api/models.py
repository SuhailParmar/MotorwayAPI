from django.db import models


class MotorwayEvent(models.Model):
    event_id = models.IntegerField(primary_key=True, editable=False)
    motorway = models.IntegerField(max_length=2)
    direction = models.CharField(max_length=1)
    metadata = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=255)
    time_day_worded = models.CharField(max_length=3)
    time_day_numerical = models.IntegerField(max_length=2)
    time_hour = models.IntegerField(max_length=2)
    time_minutes = models.IntegerField(max_length=2)
    time_seconds = models.IntegerField(max_length=2)
    time_timestamp = models.IntegerField(max_length=2)
    time_year = models.IntegerField(max_length=4)

    # Missing Junction

