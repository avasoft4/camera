import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.OUT)
def capture():
    print('Capturing image')
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/picture.jpg')
    print('Image Captured')
    camera.stop_preview()
    exit()
def record():
    print('Recording Video')
    camera = PiCamera()
    camera.start_preview()
    camera.start_recording('/home/pi/video.h264')
    sleep(5)
    camera.stop_recording()
    print('Video Recorded')
    camera.stop_preview()
    exit()
try:
    while True:
         button_state = GPIO.input(17)
         button_state1 = GPIO.input(22)
         if button_state == False:
             GPIO.output(27, True)
             sleep(0.5)
             GPIO.output(27, False)
             capture()
             sleep(0.2)
         elif button_state1 == False:
             GPIO.output(27, True)
             sleep(0.5)
             GPIO.output(27, False)
             record()
             sleep(0.2)
         else:
             GPIO.output(27, False)
except:
    GPIO.cleanup()
