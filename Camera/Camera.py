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
import picamera         # Used to control the camera module

# from PIL import Image   # Used to modify the image (rotate)


class Camera:
    def __init__(self, debug=False):
        self.debug = debug

    def take_picture(self, photo_name):
        with picamera.PiCamera() as camera:
            # Take photo and save to disc
            camera.start_preview()
            time.sleep(2)
            camera.resolution = (1024, 768)
            camera.exposure_mode = 'auto'
            camera.capture(photo_name)

            # Rotate photo to compensate for rotational position in case
            # flip_vert = Image.open(photo_name).transpose(Image.FLIP_TOP_BOTTOM)
            # flip_vert.save(photo_name, quality=100)
            # flip_horiz = Image.open(photo_name).transpose(Image.FLIP_LEFT_RIGHT)
            # flip_horiz.save(photo_name, quality=100)

            return True

