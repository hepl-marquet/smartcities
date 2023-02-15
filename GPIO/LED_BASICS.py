#15/02/23 vincent.marquet@student.hepl.be
#LED_BASICS.py
#Programme qui allume ou éteint une LED connectée au port 16

#Importation de la librairie
import machine

#Définition de la Pin et de son utilisation
LED = machine.Pin(16,machine.Pin.OUT)

#Si on met la valeur à 1, la LED s'allume si on met la valeur à 0, elle s'éteint.
LED.value(0)