#20/04/23 vincent.marquet@student.hepl.be
#PIR_SENSOR_BASICS.py
#Programme qui permet de détecter un mouvement et de le dire dans la console toutes les 8 secondes.

#Importation des librairies
from machine import Pin
from utime import sleep

#Déclaration des Pins et variables
#Capteur de lumière pin ADC(0)
PIR = Pin(18, Pin.IN)

#Boucle de lecture
while True:
    #On fait une condition pour voir si le capteur détecte un mouvement.
    if PIR.value() == 1:
        #On affiche "Mouvement détecté"
        print('Mouvement détecté')
    elif PIR.value() == 0:
        #On affiche "Pas de mouvement détecté"
        print('Pas de mouvement détecté')
    sleep(8)

    
