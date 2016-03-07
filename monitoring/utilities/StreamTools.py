import socket
import time
import picamera
from django.conf import settings

class StreamTools(object):
    """
    Tools for streaming with Pi Camera.
    """

    def __init__(self):
        self.stream_server = settings.PYGROW_SERVER_IP
        self.stream_port = int(settings.PYGROW_STREAM_PORT)
        self.stream_type = 'h264'
        self.stream_length = 60

    def stream(self):
        # Connect a client socket to server:port (localhost:7777)
        client_socket = socket.socket()
        client_socket.connect((self.stream_server, self.stream_port))

        # Make a file-like object out of the connection
        connection = client_socket.makefile('wb')
        try:
            with picamera.PiCamera() as camera:
                camera.resolution = (640, 480)
                camera.framerate = 24
                # Start a preview and let the camera warm up for 2 sec
                # camera.start_preview()
                time.sleep(2)
                # Start video recording
                camera.start_recording(connection, format=self.stream_type)
                # Send the output to the connection for the length of the stream
                camera.wait_recording(self.stream_length)
                # Stop video recording
                camera.stop_recording()
        finally:
            connection.close()
            client_socket.close()
