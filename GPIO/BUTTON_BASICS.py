#15/02/23 vincent.marquet@student.hepl.be
#BUTTON_BASICS.py
#Programme qui permet d'allumer/éteindre une LED à l'aide d'un bouton poussoir

#Importation de la librairie principale
import machine

#Définition des Pins et de leurs utilisations
LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)

#Boucle WHILE qui vérifie si l'on appuie sur le bouton
while True:
    BUTTON_VAL = BUTTON.value() 	#Valeur du bouton
    if BUTTON_VAL == 1:				#Cas si on appuie sur le bouton
        LED.value(1)				#Allume la LED
    elif BUTTON_VAL == 0:			#Cas si on appuie pas sur le bouton
        LED.value(0)				#Éteint la LED