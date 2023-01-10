# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import io
import numpy as np
import base64
import time
from flood import flood

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 24
time.sleep(2)

count = 0

rawCapture = PiRGBArray(camera, size=(320,240))

def as_bytes(image):
        bytes = np.ndarray.tobytes(image)
        return bytes
        


def getFrame():
        try:
                for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                        image = frame.array
                        ##yield as_bytes(image)
                        yield image
                        rawCapture.seek(0)
                        rawCapture.truncate()
        except KeyboardInterrupt:
                print('Hello user you have pressed ctrl-c button.')
        finally:
                print('closing camera')
                camera.close()


def getFrameFactory():
        return getFrame