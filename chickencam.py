#!/usr/bin/env python

""""
    File name: chickencam.py
    Purpose: script to take pictures. OF CHICKENS!!!
    Author: Jason Bettineski
    Date created: 8/11/2017
    Python Version: 3.0
"""

import time
from Camera.Camera import Camera


while True:
    # Create camera object and take picture

    camera = Camera()

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    photo_file_name = '/home/pi/python/ChickenCam/photos/%s.jpg' % timestamp
    photo_location = camera.take_picture(photo_file_name)

    time.sleep(15)
