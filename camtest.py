from picamera import PiCamera
from time import sleep

cam = PiCamera()

for i in range(10):
	sleep(3)
	cam.capture('/home/kofimeighan/testcode/images/image{}.jpg'.format(i))
