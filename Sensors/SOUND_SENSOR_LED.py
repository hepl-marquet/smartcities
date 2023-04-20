#20/04/23 vincent.marquet@student.hepl.be
#SOUND_SENSOR_LED.py
#Programme qui permet d'allumer plus ou  moins fort une LED en fonction du volume ambiant.

#Importation des librairies.
from machine import ADC, Pin, PWM

#Déclaration des Pins.
#Capteur de son : PIN A0, range de 0-65535 soit 16bits.
SOUND_SENSOR = ADC(0)
#LED : PIN D18
LED_PWM = PWM(Pin(18))
#Fréquence de la LED
LED_PWM.freq(500)


#Boucle de lecture.
while True:
    #Déclaration de la variable "average" qui sera la moyenne des mesures effectuées.
    average = 0
    #On crée une boucle for qui va s'effectuer 1000 fois.
    for i in range (1000):
        #On enregistre la valeur lue dans la variable "noise".
        noise = SOUND_SENSOR.read_u16()
        #On additione tous les échantillons.
        average += noise
    #Calcul de la moyenne.
    average = average/1000
    #On teste si la moyenne est à un certain barème et en fonction du barème, on allume plus ou moins fort la LED.
    if average <= 9000:
        LED_PWM.duty_u16(0)
    elif average > 9000 and average <= 12000:
        LED_PWM.duty_u16(15000)
    elif average > 12000:
        LED_PWM.duty_u16(65535)