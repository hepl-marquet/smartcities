#16/02/23 vincent.marquet@student.hepl.be
#PWM_POTENTIOMETER_LED.py
#Programme qui permet de controller la luminosité d'une LED à l'aide du potentiomètre

#Importation des librairies
from machine import Pin,ADC,PWM

#Déclaration de la Pin
Potentiometre = ADC(0)						#Potentiomètre : PIN A0
LED_PWM = PWM(Pin(18))						#LED : PIN D18
LED_PWM.freq(500)                           #Frequence de la LED

#Boucle de lecture
while True:
    LED_PWM.duty_u16(Potentiometre.read_u16() )					#Variation du duty cycle, cela correspond à la période pendant laquelle l'impulsion est positive par rapport à la période total d'un cycle, et on controle le duty cyvle avec la valeur du potentiomètre qui est déjà ajusté avec la range de la LED
