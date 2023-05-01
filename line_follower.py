import cv2
import numpy as np
from simple_pid import PID
import logging

class LineFollower:
	'''
	OpenCV based controller
	This controller takes a horizontal slice of the image at a set Y coordinate.
	Then it converts to HSV and does a color thresh hold to find the yellow pixels.
	It does a histogram to find the pixel of maximum yellow. Then is uses that iPxel
	to guid a PID controller which seeks to maintain the max yellow at the same point
	in the image.
	'''

	SCAN_Y = 120
	SCAN_HEIGHT = 20
	COLOR_THRESHOLD_LOW = np.array([0, 50, 50])
	COLOR_THRESHOLD_HIGH = np.array([50, 255, 255])

	TARGET_THRESHOLD = 10
	CONFIDENCE_THRESHOLD = ( 1 / 2592 ) / 3

	THROTTLE_MAX = 0.3
	THROTTLE_MIN = 0.15
	THROTTLE_INITIAL = THROTTLE_MIN
	THROTTLE_STEP = 0.05

	PID_P = -0.01
	PID_I = 0.000
	PID_D = -0.0001


	def get_i_color(self, cam_img)
		'''
        get the horizontal index of the color at the given slice of the image
        input: cam_image, an RGB numpy array
        output: index of max color, value of cumulative color at that index, and mask of pixels in range
        '''

        # take a horizontal slice of the image
        iSlice = SCAN_Y
        scan_line = cam_img[iSlice : iSlice + self.SCAN_HEIGHTN, :, :]

        # convert to HSV color space
        img_hsv = cv2.cvtColor(scan_line, cv2.COLOR_RGB2HSV)

        # make a mask of the colors in our range we are looking for
        mask = cv2.inRange(img_hsv, self.color_thr_low, self.color_thr_hi)

        # which index of the range has the highest amount of yellow?
        hist = np.sum(mask, axis=0)
        max_yellow = np.argmax(hist)

        return max_yellow, hist[max_yellow], mask