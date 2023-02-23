#16/02/23 vincent.marquet@student.hepl.be
#BONUS_BUZZER_POTENTIOMETER.py
#Programme qui permet de controller la note de musique du buzzer à l'aide du potentiomètre

#Importation des librairies
from machine import ADC,Pin,PWM
from utime import sleep

#Déclaration des Pins et variables
ROTARY_ANGLE_SENSOR = ADC(0)				#Potentiomètre : PIN A0
buzzer = PWM(Pin(27))						#Buzzer :        PIN A1
Pot = 0

#Boucle de lecture
while True:
    print(ROTARY_ANGLE_SENSOR.read_u16()) 	#Affiche la valeur du potentiomètre
    Pot = ROTARY_ANGLE_SENSOR.read_u16()		#Insère la valeur dans la variable "a"
    buzzer.duty_u16(500)					#Volume du buzzer
    if 5000 >= Pot and Pot >= 0:				#Différentes notes attribués à certaines valeurs obtenues par le potentiomètre.
        buzzer.freq(261)					#DO
    elif 10000 >= Pot and Pot >= 5000:
        buzzer.freq(293)					#RE
    elif 15000 >= Pot and Pot >= 10000:
        buzzer.freq(329)					#MI
    elif 20000 >= Pot and Pot >= 15000:
        buzzer.freq(349)					#FA
    elif 25000 >= Pot and Pot >= 20000:
        buzzer.freq(392)					#SOL
    elif 30000 >= Pot and Pot >= 25000:
        buzzer.freq(440)					#LA
    elif 35000 >= Pot and Pot >= 30000:
        buzzer.freq(493)					#SI
    sleep(0.5)								#Temps de lecture de la note
