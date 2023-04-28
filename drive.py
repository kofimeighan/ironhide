import torch
import clip
import RPi.GPIO as GPIO
from time import sleep
from PIL import Image
from picamera import PiCamera
from torchsummary import summary

device = 'cuda' if torch.cuda.is_available() else "cpu"

print(f'Using device: {device}')

model, preprocess = clip.load("ViT-B/32", device = device)
print(model)
#print(summary(model, (3, 32, 32)))

SERVO_PWM = 11
MOTOR_PWM = 32
MOTOR_AIN1 = 16
MOTOR_AIN2 = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#SERVO
GPIO.setup(SERVO_PWM, GPIO.OUT)
servo = GPIO.PWM(SERVO_PWM)
#MOTOR, either or i think ????
GPIO.setup(MOTOR_PWM, GPIO.OUT)
motor = GPIO.PWM(MOTOR_PWM)

#MOTOR
GPIO.setup(MOTOR_AIN1, GPIO.OUT)
GPIO.setup(MOTOR_AIN2, GPIO.OUT)

#setup camera
camera = PiCamera()

img_num = 0
while True:
	cam.capture('/home/kofimeighan/testcode/images/image{}.jpg'.format(img_num))
	sleep(3)
	img = Image.open('/home/kofimeighan/testcode/images/image{}.jpg'.format(img_num))



	img_num = img_num + 1


GPIO.cleanup()

#SETUP AUTOMATIC IMAGE OVERWRITING AND DELETION

#def run(self, cam_img):	



