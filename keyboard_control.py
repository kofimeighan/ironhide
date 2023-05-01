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

#motor.start(100)
#servo.start(0)


HIGH = GPIO.HIGH
LOW = GPIO.LOW

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
    duty = angle / 18 + 2.5
    GPIO.output(SERVO_PWM, HIGH)
    servo.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(SERVO_PWM, LOW)
    servo.ChangeDutyCycle(0)

def move_right():
    #GPIO.output(SERVO_PWM, HIGH)
    servo.ChangeDutyCycle(5.5)
    sleep(0.3)
    #servo.ChangeDutyCycle(7.5)
    #sleep(2)
   # GPIO.output(SERVO_PWM, LOW)

def move_left():
    #GPIO.output(SERVO_PWM, HIGH)
    duty = 7.5 + 1
    #while duty <= 12:
    #    servo.ChangeDutyCycle(duty)
    #    sleep(1)
    #    duty = duty + 1
    servo.ChangeDutyCycle(9.5)
    sleep(0.3)
    #servo.ChangeDutyCycle(7.5)
    #sleep(2)
    #GPIO.output(SERVO_PWM, LOW)

def move_forward():
    GPIO.output(STDBY, HIGH)
    GPIO.output(AIN1, LOW)
    GPIO.output(AIN2, HIGH)
    motor.ChangeDutyCycle(50)
    sleep(0.5)
    motor.ChangeDutyCycle(0)
    GPIO.output(STDBY, LOW)
    servo.ChangeDutyCycle(7.5)

def move_backward():
    GPIO.output(STDBY, HIGH)
    GPIO.output(AIN1, HIGH)
    GPIO.output(AIN2, LOW)
    motor.ChangeDutyCycle(50)
    sleep(0.5)
    motor.ChangeDutyCycle(0)
    GPIO.output(STDBY, LOW)
    servo.ChangeDutyCycle(7.5)

def main():
    #GPIO.output(STDBY, GPIO.HIGH)
    motor.start(0)
    servo.start(0)
    #sleep(1)

    while True:
        char = getch()

        if(char == "w"):
            print("FORWARD")
            move_forward()

        if(char == "s"):
            print("BACKWARD")
            move_backward()

        if(char == "a"):#LEFT
            print("LEFT")
            move_left()

        if(char == "d"):#RIGHT
            print("RIGHT")
            move_right()

        if(char == "x"):
            print("STOPPING")
            #GPIO.output(STDBY, GPIO.LOW)
            #servo.ChangeDutyCycle(8)
            motor.stop()
            servo.stop()
            GPIO.cleanup()
            break

        #sleep(0.5)
        char = ""

if __name__ == "__main__":
    main()
