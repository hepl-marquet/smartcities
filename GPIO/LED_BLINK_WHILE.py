#15/02/23 vincent.marquet@student.hepl.be
#LED_BLINK_WHILE.py
#Programme qui fait clignoter une LED connectée au port 16 indéfiniment

#Importation de la librairie principale
import machine
#Importation de la librairie du temps
import utime

#Définition de la Pin et de son utilisation
LED = machine.Pin(16,machine.Pin.OUT)

#Boucle WHILE infinie
while True:
    LED.value(1) 	#Allume la LED
    utime.sleep(1) 	#Fait une pause pendant 1 seconde
    LED.value(0) 	#Éteint la LED
    utime.sleep(1) 	#Fait une pause pendant 1 seconde