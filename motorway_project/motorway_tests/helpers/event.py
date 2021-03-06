class Event():
    """
    Python representation of a motorway_event
    """

    def __init__(self, **kwargs):
        """
        Provide default arguments for an event
        """
        self.closest_cities = kwargs.get('closest_cities', [
            "Stafford (N)",
            "Stoke / Newcastle-u-Lyme"
        ])
        self.direction = kwargs.get('direction', "n")
        self.event_id = kwargs.get('event_id', 1052482906797428737)
        self.junction = kwargs.get('junction', [14, 15])
        self.metadata = kwargs.get(
            'metadata', "Event Generated by Tweet Miner at 2018-10-20T20:50:12.286910")
        self.motorway = kwargs.get('motorway', 6)
        self.reason = kwargs.get('reason', "congestion")
        self.time_day_numerical = kwargs.get('time_day_numerical', 17)
        self.time_day_worded = kwargs.get('time_day_worded', "Wed")
        self.time_hour = kwargs.get('time_hour', 8)
        self.time_minutes = kwargs.get('time_minutes', 54)
        self.time_seconds = kwargs.get('time_seconds', 13)
        self.time_timestamp = kwargs.get(
            'time_timestamp', "2018-10-17T08:54:13Z")
        self.time_year = kwargs.get('time_year', 2018)

    def build_payload(self):
        payload = {
            "closest_cities": self.closest_cities,
            "direction": self.direction,
            "event_id": self.event_id,
            "junction": self.junction,
            "metadata": self.metadata,
            "motorway": self.motorway,
            "reason": self.reason,
            "time_day": self.time_day_numerical,
            "time_day_worded": self.time_day_worded,
            "time_hour": self.time_hour,
            "time_minutes": self.time_minutes,
            "time_seconds": self.time_seconds,
            "time_timestamp": self.time_timestamp,
            "time_year": self.time_year,
            "extra_information": []
        }
        return payload
