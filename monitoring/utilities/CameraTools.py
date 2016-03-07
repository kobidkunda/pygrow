import time
import subprocess
import picamera
from django.conf import settings
# Use to ensure Pi Camera LED is off
# import RPi.GPIO as GPIO


class CameraTools(object):
    """
    Tools for working with Pi Camera.
    """

    ### Pi Camera Default Settings
    # https://www.raspberrypi.org/documentation/raspbian/applications/camera.md

    # camera.sharpness = 0
    # camera.contrast = 0
    # camera.brightness = 50
    # camera.saturation = 0
    # camera.ISO = 0
    # camera.video_stabilization = False
    # camera.exposure_compensation = 0
    # camera.exposure_mode = 'auto'
    # camera.meter_mode = 'average'
    # camera.awb_mode = 'auto'
    # camera.image_effect = 'none'
    # camera.color_effects = None
    # camera.rotation = 0
    # camera.hflip = False
    # camera.vflip = False
    # camera.crop = (0.0, 0.0, 1.0, 1.0)

    def __init__(self):
        self.type = 'Pi'
        # Pi Camera Photo options
        self.photo_cmd = 'raspistill'
        self.photo_path = settings.BASE_DIR + '/photos/'
        self.photo_format = '.png'
        # Pi Camera Video options
        self.video_cmd = 'raspivid'
        self.video_path = settings.BASE_DIR + '/videos/'
        self.video_format = '.h264'
        # Timestamp format for photos and videos
        self.timestamp = time.strftime('%Y-%m-%d_%H%M%S')

    def photo(self):
        """
        Take photo with Pi Camera.
        """
        # cmd = self.photo_cmd + \
        #     ' -o' + self.photo_path + \
        #     ' -t 1000' \
        #     ' -w 640' \
        #     ' -t 480' \
        #     ' -rot 0' \
        # subprocess.call(cmd, shell=True)
        # time.sleep(4)
        with picamera.PiCamera() as camera:
            # Set filename for photo
            camera.capture(self.photo_path + 'photo_' + self.timestamp + self.photo_format)

    def timelapse(self, duration, interval):
        """
        Record timelapse with Pi Camera.
        """
        # Use raspistill timelapse functionality
        # http://picamera.readthedocs.org/en/release-1.10/recipes1.html#capturing-timelapse-sequences

        # camera.resolution = (1280, 720)
        # camera.framerate = 30
        # Wait for the automatic gain control to settle
        # time.sleep(2)
        # Now fix the values
        # camera.shutter_speed = camera.exposure_speed
        # camera.exposure_mode = 'off'
        # g = camera.awb_gains
        # camera.awb_mode = 'off'
        # camera.awb_gains = g
        # Finally, take several photos with the fixed settings
        # camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])

        # with picamera.PiCamera() as camera:
        #     camera.start_preview()
        #     time.sleep(2)
        #     for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        #         print('Captured %s' % filename)
        #         # Wait 5 minutes
        #         time.sleep(interval)
        pass

    def video(self, duration):
        """
        Record video with Pi Camera.
        """
        # cmd = self.video_cmd + \
        #     ' -o' \
        #     self.video_path
        # subprocess.call(cmd, shell=True)
        with picamera.PiCamera() as camera:
            # Set filename for video
            camera.start_recording(self.video_path + 'video_' + self.timestamp + self.video_format)
            # Record for the duration
            time.sleep(int(duration))
            # Stop video recording
            camera.stop_recording()

    def overlay_text():
        # http://picamera.readthedocs.org/en/release-1.10/recipes1.html#overlaying-text-on-the-output
        # camera.annotate_text = 'PyGrow'

        # TODO: Add ability to overlay text or a timestamp
        pass