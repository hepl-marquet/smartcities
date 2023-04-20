#20/04/23 vincent.marquet@student.hepl.be
#LIGHT_SENSOR_BASICS.py
#Programme qui permet d'afficher la valeur lue par le capteur de luminosité toutes les secondes.

#Importation des librairies
from machine import ADC, PWM, Pin
from utime import sleep

#Déclaration des Pins et variables
#Capteur de lumière pin ADC(0)
LIGHT_SENSOR = ADC(0)
#Buzzer pin ADC(1)
Buzzer = PWM(Pin(27))
#Fréquence du buzzer
Buzzer.freq(1046)

#Boucle de lecture
while True:
    #On fait une condition pour voir si la lumière est allumée
    if LIGHT_SENSOR.read_u16() >= 25000:
        #On règle le volume du buzzer
        Buzzer.duty_u16(1000)
        #On fait sonner pendant 1 seconde
        sleep(1)
    #On coupe le volume
    Buzzer.duty_u16(0)
    