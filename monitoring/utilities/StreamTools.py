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
        """
        Stream Pi Camera video over socket.
        """
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.framerate = 24

            # Create socket on server:port (localhost:7777)
            server_socket = socket.socket()
            server_socket.bind((self.stream_server, self.stream_port))
            server_socket.listen(0)

            # Accept a single connection and make a file-like object out of it
            connection = server_socket.accept()[0].makefile('wb')
            try:
                # Start video recording
                camera.start_recording(connection, format=self.stream_type)
                # Send the output to the connection for the length of the stream
                camera.wait_recording(self.stream_length)
                # Stop video recording
                camera.stop_recording()
            finally:
                connection.close()
                server_socket.close()
