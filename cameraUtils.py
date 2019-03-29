"""
Camera utilities for TESSR

Version 1.0
>Basic capture and storage
"""

#Get dependencies
import time
from picamera import PiCamera

camera = PiCamera()

def captureImage():
	#Captures and stores a still image
	time.sleep(1)
	camera.capture("Images/"+time.asctime().replace(" ","_")+".jpg") #Check path
