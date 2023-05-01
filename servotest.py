import RPi.GPIO as GPIO
from time import sleep

#PIN DEFINITIONS
SERVO_PWM = 11
MOTOR_AIN1 = 16
MOTOR_AIN2 = 15
MOTOR_PWM = 32

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(SERVO_PWM, GPIO.OUT)
GPIO.setup(MOTOR_PWM, GPIO.OUT)
GPIO.setup(MOTOR_AIN1, GPIO.OUT)
GPIO.setup(MOTOR_AIN2, GPIO.OUT)


#motor = GPIO.PWM(MOTOR_PWM)
servo = GPIO.PWM(SERVO_PWM, 50)

print("TESTING SERVO")
servo.start(7.5)
sleep(1)
duty_servo = 5

try:
	while duty_servo <= 10:
		servo.ChangeDutyCycle(duty_servo)
		sleep(2)
		duty_servo = duty_servo + 1

	servo.ChangeDutyCycle(7.5)
	sleep(2)
except KeyvoardInterrupt:
	servo.stop()
	GPIO.cleanup(SERVO_PWM)
