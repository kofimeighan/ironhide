import RPi.GPIO as GPIO
from time import sleep

#PIN DEFINITIONS
AIN1 = 16
AIN2 = 15
PWM = 32
STDBY = 22
PWM_FREQ = 100


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PWM, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(STDBY, GPIO.OUT)

pwma = GPIO.PWM(PWM, PWM_FREQ)
pwma.start(100)


def runMotor():
	print("TESTING MOTOR")
	GPIO.output(STDBY, GPIO.HIGH)
	in1 = GPIO.HIGH
	in2 = GPIO.LOW

	GPIO.output(AIN1, in1)
	GPIO.output(AIN2, in2)
	pwma.changeDutyCycle(50)

	sleep(10)

	GPIO.output(STDBY, GPIO.LOW)
	GPIO.cleanup()
	print("done testing motor")


if __name__ == "__main__":
	runMotor()