import RPi.GPIO as GPIO
from time import sleep

#PIN DEFINITIONS
SERVO_PWM = 11
MOTOR_AIN1 = 16
MOTOR_AIN2 = 15
MOTOR_PWM = 32

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTOR_PWM, GPIO.OUT)
GPIO.setup(MOTOR_AIN1, GPIO.OUT)
GPIO.setup(MOTOR_AIN2, GPIO.OUT)


print("TESTING MOTOR")
GPIO.output(MOTOR_PWM, GPIO.HIGH)
GPIO.output(MOTOR_AIN1, GPIO.HIGH)
GPIO.output(MOTOR_AIN2, GPIO.LOW)

time.sleep(10)

GPIO.output(MOTOR_PWM, GPIO.HIGH)
GPIO.output(MOTOR_AIN1, GPIO.LOW)
GPIO.output(MOTOR_AIN2, GPIO.HIGH)

time.sleep(10)

GPIO.cleanup()
print("done testinh motor")
