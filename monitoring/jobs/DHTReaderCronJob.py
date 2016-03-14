from django.conf import settings
from django_cron import CronJobBase, Schedule
from .utilities import DHTTools
from monitoring.models import TemperatureReading, HumidityReading


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

        print(reading)

        # Save TemperatureReading to database
        temperature = TemperatureReading()
        # temperature.sensor = sensor
        # temperature.measurement_type = measurement_type
        temperature.timestamp = reading['timestamp']
        temperature.value = reading['temperature']
        temperature.save()

        print(reading['temperature'])

        # Save HumidityReading to database
        humidity = humidityReading()
        # humidity.sensor = sensor
        humidity.timestamp = reading['timestamp']
        humidity.value = reading['humidity']
        humidity.save()

        print(reading['humidity'])
