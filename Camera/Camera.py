#!/usr/bin/env python

""""
    File name: Camera.py
    Purpose: Class to interface with PiCamera
    Author: Jason Bettineski
    Date created: 6/12/2017
    Date last modified: 6/12/2017
    Python Version: 3.0
"""

import time             # Used to generate timestamp filename
from PIL import Image   # Used to modify the image (rotate)
import picamera         # Used to control the camera module


class Camera:
    def __init__(self, debug=False):
        self.debug = debug

    def take_picture(self):
        with picamera.PiCamera() as camera:
            # Create timestamp string for filename
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            photo_file_name = '/home/pi/python/chickencam/photos/%s.jpg' % timestamp

            # Take photo and save to disck
            if self.debug: print("Camera.Camera: Taking Photo")
            camera.start_preview()
            time.sleep(2)
            camera.resolution = (3280, 2464)
            camera.exposure_mode = 'auto'
            camera.capture(photo_file_name)
            if self.debug: print("Photo saved to disc")

            # Rotate photo to compensate for rotational position in case
            flip_vert = Image.open(photo_file_name).transpose(Image.FLIP_TOP_BOTTOM)
            flip_vert.save(photo_file_name, quality=100)
            flip_horiz = Image.open(photo_file_name).transpose(Image.FLIP_LEFT_RIGHT)
            flip_horiz.save(photo_file_name, quality=100)
            if self.debug: print("Photo rotated successfully")

        return photo_file_name