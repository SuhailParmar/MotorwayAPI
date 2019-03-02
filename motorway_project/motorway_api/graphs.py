import logging
from .models import MotorwayEvent
class Graphs:
    @staticmethod
    def iqp(qp):
        for q in qp:
            logging.warning(q.event_id)

