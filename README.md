PyGrow
======

A Python and Django project to monitor an environment with a Raspberry Pi using a Pi Camera and DHT temperature/humidity sensor. Alerts can be received via email or SMS.


Features
--------

- Use Pi Camera for monitoring
- Use Pi Camera for photos
- Use Pi Camera for timelapses
- Use DHT temperature sensor for monitoring
- Use DHT humidity sensor for monitoring
- Store photos/videos on device
- Store sensor data in database
- Add management for groups and permissions
- Add user accounts and logins


Usage
-----

Use Ansible to install on Raspberry Pi running Raspbian or Ubuntu Mate.

Ensure Pi Camera is enabled:
[https://www.raspberrypi.org/documentation/usage/camera/README.md](https://www.raspberrypi.org/documentation/usage/camera/README.md)

Test raspistill CLI tool (1 photo):
```
$ raspistill -o test-photo.jpg
```

Test raspivid CLI tool (5 second video):
```
$ raspivid -o test-video.h264 -t 10000
```


Materials
---------

Base:

- Raspberry Pi 2 Model B or 3 Model B
- microSD card with Raspbian or Ubuntu Mate
- 5V micro USB power cable

Peripherals:

- Raspberry Pi camera
- DHT11 or DHT22 temperature/humidity sensor w/ cable


To Do
-----

- Add camera/temp/humidity status in the sidebar
- Add photo capability with raspistill
- Add timelapse capability with raspistill
- Add video capability with raspivid
- Add email alerts/notifications (Django emails)
- Add SMS alerts/notifications (Twilio)


Author
------

Peter Schaadt

[https://github.com/peterfschaadt](https://github.com/peterfschaadt)

[http://peterschaadt.com](http://peterschaadt.com)
