from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


def validate_only_one_instance(object):
    """
    Validate that only one instance of a model exists.
    """
    model = object.__class__
    if (model.objects.count() > 0 and object.id != model.objects.get().id):
        raise ValidationError('Only one instance of model %s allowed.' % model.__name__)


#
### Camera and Camera Settings
#

class Camera(models.Model):
    """
    Model for Camera.
    - type
    - name
    - enabled
    """

    CAMERA_TYPES=(
        ('Pi', 'Pi Camera'),
    )
    type = models.CharField(
        choices=CAMERA_TYPES,
        max_length=1
    )
    name = models.CharField(
        max_length=30,
        blank=False
    )
    enabled = models.BooleanField(
        default=False
    )

    def __unicode__(self):
        return u'%s' % (self.name)

    def clean(self):
        # Only allow one instance of Camera model
        validate_only_one_instance(self)

    def save(self, *args, **kwargs):
        super(Camera, self).save(*args, **kwargs)
        self.full_clean()
        if not self.name:
            self.name = 'Camera' + str(self.id)
            self.save()


class CameraSettings(models.Model):
    """
    Model for Camera Settings.
    - sharpness
    - contrast
    - brightness
    - saturation
    - iso
    - video_stabilization
    - exposure_compensation
    - exposure_mode
    - white_balance
    - rotation
    - image_quality
    - video_bitrate
    """

    sharpness = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(-100),
            MaxValueValidator(100)
        ]
    )
    contrast = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(-100),
            MaxValueValidator(100)
        ]
    )
    brightness = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    saturation = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(-100),
            MaxValueValidator(100)
        ]
    )
    iso = models.IntegerField(
        default=100,
        validators=[
            MinValueValidator(100),
            MaxValueValidator(800)
        ]
    )
    video_stabilization = models.BooleanField(
        default=True
    )
    exposure_compensation = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(-10),
            MaxValueValidator(10)
        ]
    )
    EXPOSURE_MODE_TYPES=(
        ('Auto', 'Auto'),
        ('On', 'On'),
        ('Off', 'Off'),
    )
    exposure_mode = models.CharField(
        choices=EXPOSURE_MODE_TYPES,
        max_length=1
    )
    WHITE_BALANCE_TYPES=(
        ('Auto', 'Auto'),
        ('On', 'On'),
        ('Off', 'Off'),
    )
    white_balance = models.CharField(
        choices=WHITE_BALANCE_TYPES,
        max_length=1
    )
    rotation = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(4)
        ]
    )
    image_quality = models.IntegerField(
        default=85,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    video_bitrate = models.IntegerField(
        default=17000000,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(25000000)
        ]
    )

    def clean(self):
        # Only allow one instance of CameraSettings model
        validate_only_one_instance(self)

    def save(self, *args, **kwargs):
        super(CameraSettings, self).save(*args, **kwargs)
        self.full_clean()
        self.save()

#
### Temperature Sensor, Settings, and Readings
#

class TemperatureSensor(models.Model):
    """
    Model for Temperature Sensor.
    - type
    - name
    - enabled
    """

    TEMP_SENSOR_TYPES=(
        ('D11', 'DHT11'),
        ('D22', 'DHT22'),
    )
    type = models.CharField(
        choices=TEMP_SENSOR_TYPES,
        max_length=1
    )
    name = models.CharField(
        max_length=30,
        blank=False
    )
    enabled = models.BooleanField(
        default=False
    )

    def __unicode__(self):
        return u'%s' % (self.name)

    def clean(self):
        # Only allow one instance of TemperatureSensor model
        validate_only_one_instance(self)

    def save(self, *args, **kwargs):
        super(TemperatureSensor, self).save(*args, **kwargs)
        self.full_clean()
        if not self.name:
            self.name = 'TemperatureSensor' + str(self.id)
            self.save()


class TemperatureSensorSettings(models.Model):
    """
    Model for Temperature Sensor Settings.
    - measurement_type
    """

    MEASUREMENT_TYPES=(
        ('F', 'Fahrenheit'),
        ('C', 'Celsius'),
    )
    measurement_type = models.CharField(
        choices=MEASUREMENT_TYPES,
        max_length=1
    )

    def clean(self):
        # Only allow one instance of TemperatureSensorSettings model
        validate_only_one_instance(self)

    def save(self, *args, **kwargs):
        super(TemperatureSensorSettings, self).save(*args, **kwargs)
        self.full_clean()
        self.save()


class TemperatureReading(models.Model):
    """
    Model for Temperature Reading.
    - measurement_type
    - timestamp
    - value
    """

    MEASUREMENT_TYPES=(
        ('F', 'Fahrenheit'),
        ('C', 'Celsius'),
    )
    measurement_type = models.CharField(
        choices=MEASUREMENT_TYPES,
        max_length=1
    )
    timestamp = models.DateTimeField(
        default=timezone.now
    )
    value = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )


#
### Humidity Sensor, Settings, and Readings
#

class HumiditySensor(models.Model):
    """
    Model for Humidity Sensor.
    - type
    - name
    - enabled
    """

    HUMID_SENSOR_TYPES=(
        ('D11', 'DHT11'),
        ('D22', 'DHT22'),
    )
    type = models.CharField(
        choices=HUMID_SENSOR_TYPES,
        max_length=1
    )
    name = models.CharField(
        max_length=30,
        blank=False
    )
    enabled = models.BooleanField(
        default=False
    )

    def __unicode__(self):
        return u'%s' % (self.name)

    def clean(self):
        # Only allow one instance of HumiditySensor model
        validate_only_one_instance(self)

    def save(self, *args, **kwargs):
        super(HumiditySensor, self).save(*args, **kwargs)
        self.full_clean()
        if not self.name:
            self.name = 'HumiditySensor' + str(self.id)
            self.save()


class HumidityReading(models.Model):
    """
    Model for Humidity Reading.
    - timestamp
    - value
    """

    timestamp = models.DateTimeField(
        default=timezone.now
    )
    value = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )


class TimelapseSettings(models.Model):
    """
    Model for Timelapse Settings.
    - name
    - enabled
    - interval
    - duration
    """

    name = models.CharField(
        max_length=30,
        blank=False
    )
    enabled = models.BooleanField(
        default=False
    )
    interval = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )
    duration = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )

    def __unicode__(self):
        return u'%s' % (self.name)

    def clean(self):
        # Only allow one instance of TimelapseSettings model
        validate_only_one_instance(self)

    def save(self, *args, **kwargs):
        super(Camera, self).save(*args, **kwargs)
        self.full_clean()
        if not self.name:
            self.name = 'Timelapse ' + str(self.id)
            self.save()


#
### Email Alerts
#

class EmailAlert(models.Model):
    """
    Model for Email Alert.
    - timestamp
    - end
    - recipient
    - include_photo
    - min_temperature
    - max_temperature
    - min_humidity
    - max_humidity
    """

    timestamp = models.DateTimeField(
        default=timezone.now
    )
    end = models.DateTimeField()
    recipient = models.EmailField()
    include_photo = models.BooleanField()
    min_temperature = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )
    max_temperature = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )
    min_humidity = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    max_humidity = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )


class EmailPhoto(models.Model):
    """
    Model for Email Photo.
    - timestamp
    - end
    - frequency
    """

    timestamp = models.DateTimeField(
        default=timezone.now
    )
    end = models.DateTimeField()
    frequency = models.IntegerField(
        validators=[
            MinValueValidator(-150),
            MaxValueValidator(150)
        ]
    )
