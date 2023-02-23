#23/02/23 vincent.marquet@student.hepl.be
#BONUS_SERVO_POTENTIOMETER.py
#This programm controlls the angle of a servo motor using a potentiometer

#Importation of the libraries
from machine import Pin,ADC,PWM
from utime import sleep

#Pins declaration
Angle_Sensor = ADC(0)
pwm_servo = PWM(Pin(20))

#Variable declaration
B = 0																#Variable used to check if the potentiometer value has changed or not so that the servo motor doesnt update constantly but only when a major change happens (>650)
pwm_servo.freq(100) 												#Frequency of the servo that we are using in this code

#Main while loop
while True:
    A = Angle_Sensor.read_u16()										#Next value of the angle used to check the variation between two measures of the potentiometer
    if abs(A-B) > 650:
            Angle = int((Angle_Sensor.read_u16()/6.28) + 3250)		#Converting the potentiometer value to a valid angle value for the servo motor
            print(Angle)											#Printing to check the value
            pwm_servo.duty_u16(Angle)								#Setting the angle of the servo to the value we got
            sleep(0.01)												#Sleep command in order to not update too fast
            B = Angle_Sensor.read_u16()								#B takes the previous value of the angle in order to compare it to A