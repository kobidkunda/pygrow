from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#
### Camera and Camera Settings
#

class Camera(models.Model):
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


class CameraSettings(models.Model):
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


#
### Temperature Sensor and Temperature Settings
#

class TemperatureSensor(models.Model):
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

    def save(self, *args, **kwargs):
        super(TemperatureSensor, self).save(*args, **kwargs)
        if not self.name:
            self.name = 'TempSensor' + str(self.id)
            self.save()


class TemperatureSensorSettings(models.Model):
    MEASUREMENT_TYPES=(
        ('F', 'Fahrenheit'),
        ('C', 'Celsius'),
    )
    measurement_type = models.CharField(
        choices=MEASUREMENT_TYPES,
        max_length=1
    )

#
### Humidity Sensor and Humidity Settings
#

class HumiditySensor(models.Model):
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

    def save(self, *args, **kwargs):
        super(HumiditySensor, self).save(*args, **kwargs)
        if not self.name:
            self.name = 'HumiditySensor' + str(self.id)
            self.save()
