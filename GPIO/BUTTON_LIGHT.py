#15/02/23 vincent.marquet@student.hepl.be
#BUTTON_LIGHT.py
#Programme qui permet d'allumer/éteindre une LED à l'aide d'un bouton poussoir de la même manière qu'un interrupteur de la vie quotidienne

#Importation des librairies principale
from machine import Pin
from utime import sleep

#Définition des Pins et de leurs utilisations
LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)

LED_FLAG = 0 						#Initialisation du FLAG

#Boucle WHILE qui vérifie si l'on appuie sur le bouton
while True:
   if BUTTON.value() == 1:
       LED_FLAG = LED_FLAG + 1		#Incrémentation du FLAG
       sleep(0.3)					#Pause de 0,3s (nécessaire sinon à l'appui du bouton, on recevrait plusieurs appuis d'un coup dû à la rapidité de lecture de la boucle)
       if LED_FLAG == 1:			#Premier cas du FLAG (Allumer)
           LED.value(1)
       elif LED_FLAG == 2:			#Second cas du FLAG (Éteindre)
           LED_FLAG = 0				#Réinitialise le FLAG
           LED.value(0)