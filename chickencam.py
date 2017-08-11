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


debug = True            # Provides verbose messages when set to True
enable_camera = True    # Enables camera functionality when set to True
ftp_photos = False       # FTP's photos to website when set to True


if debug: print("Initializing RiverCam Device")

if enable_camera:
    # Create camera object and take picture

    if debug: print("Creating Camera object")
    camera = Camera()

    if debug: print("Camera object created. Taking picture")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    photo_file_name = '/home/pi/python/ChickenCam/photos/%s.jpg' % timestamp
    photo_location = camera.take_picture(photo_file_name)

    # If FTP functionality is enabled
    if ftp_photos:
        if debug: print("FTP image")

        ftp_uploader = FTPUploader(debug)
        ftp_uploader.upload_file('198.199.114.110',
                                 '/var/www/html/ftpup/',
                                 '/home/jason/python/rivercam/photos/image01.jpg')