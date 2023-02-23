#16/02/23 vincent.marquet@student.hepl.be
#AD_POTENTIOMETER_BASICS.py
#Programme qui permet de controller la luminosité d'une LED à l'aide du potentiomètre

#Importation des librairies
from machine import Pin,ADC,PWM

#Déclaration de la Pin
Potentiometre = ADC(0)						#Potentiomètre : PIN A0
LED_PWM = PWM(Pin(18))						#LED : PIN D18

LED_PWM.freq(100)

#Boucle de lecture
while True:
    val = Potentiometre.read_u16() 		            #Affiche la valeur du potentiomètre
    LED_PWM.duty_u16(val)					#Pause de 1 seconde
