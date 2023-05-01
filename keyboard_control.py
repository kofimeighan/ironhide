import RPi.GPIO as GPIO
from time import sleep
import sys
import tty
import termios


#PIN DEFINITIONS
AIN1 = 16
AIN2 = 15
MOTOR_PWM = 32
STDBY = 22
PWM_FREQ_MOTOR = 100
PWM_FREQ_SERVO = 50
SERVO_PWM = 11

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTOR_PWM, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(STDBY, GPIO.OUT)
GPIO.setup(SERVO_PWM, GPIO.OUT)

motor = GPIO.PWM(MOTOR_PWM, PWM_FREQ_MOTOR)
servo = GPIO.PWM(SERVO_PWM, PWM_FREQ_SERVO)

motor.start(0)
servo.start(0)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def set_angle(angle):
	duty = angle / 18 + 2
	GPIO.output(SERVO_PWM, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(SERVO_PWM, False)
	pwm.ChangeDutyCycle(0)


def move_forward():    
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(Motor_A2, GPIO.HIGH)

def move_backward():    
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(Motor_A2, GPIO.HIGH)

def main():
	while True:
		char = getch()

		if(char == "w"):
			move_forward()

		if(char == "s"): 
			move_backward()

		if(char == "a"): #LEFT
			set_angle(-90)

		if(char == "d"): #RIGHT
			set_angle(90)

		if(char == "x"):
			print("STOPPING")
			motor.stop()
			servo.stop()
			GPIO.cleanup()

		char = ""