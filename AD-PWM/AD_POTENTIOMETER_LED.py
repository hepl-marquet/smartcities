#16/02/23 vincent.marquet@student.hepl.be
#AD_POTENTIOMETER_LED.py
#Programme qui permet de controller la LED à partir de la valeur du potentiomètre

#Importation des librairies
from machine import ADC,Pin
from utime import sleep

#Déclaration des Pins
Potentiometre = ADC(0)						#Potentiomètre : PIN A0
LED = Pin(16,Pin.OUT)						#LED : PIN D16

#Boucle de lecture
while True:
    print(Potentiometre.read_u16()) 		#Affiche la valeur du potentiomètre
    if Potentiometre.read_u16() > 30000:	#Condition pour allumer la LED : valeur du potentiomètre supérieure à 30000
        LED.value(1)
        sleep(1)
    else:
        LED.value(0)
        sleep(1)