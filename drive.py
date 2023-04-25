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

SERVO_PIN = 11
MOTOR_PWM_PIN = 32
MOTOR_AIN1_PIN = 16
MOTOR_AIN2_PIN = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#SERVO
GPIO.setup(SERVO_PIN, GPIO.OUT)
#MOTOR PWM
GPIO.setup(MOTOR_PWM_PIN, GPIO.OUT)
#MOTOR
GPIO.setup(MOTOR_AIN1_PIN, GPIO.OUT)
GPIO.setup(MOTOR_AIN2_PIN, GPIO.OUT)

camera = PiCamera()

img_num = 0
while True:
	camera.capture("ROOT DIRECTORY")
	sleep(2)
	img = Image.open("IMAGE PAGE")

#SETUP AUTOMATIC IMAGE OVERWRITING AND DELETION

#def run(self, cam_img):	



