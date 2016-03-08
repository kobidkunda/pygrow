from django.conf import settings
from django_cron import CronJobBase, Schedule
from .utilities import DHTTools


class DHTReaderCronJob(CronJobBase):
    """
    Retrieve temperature and humidity values from DHT sensor.
    """
    # Run every 10 min (when DEBUG is False)
    RUN_INTERVAL = 0 if settings.DEBUG else 10

    schedule = Schedule(run_every_mins=RUN_INTERVAL)
    code = 'cron.DHTReaderCronJob'

    def do(self):
        # TODO: Check if DHT sensor is enabled
        reading = DHTTools.read_sensor()
        # TODO: Save reading to database
        print(reading)
