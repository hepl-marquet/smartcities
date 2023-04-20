#20/04/23 vincent.marquet@student.hepl.be
#PIR_SENSOR_WELCOME.py
#Programme qui détecte les mouvements et envoie un message d'accueil sur l'écran LCD.

#Importation des librairies.
from machine import Pin,I2C
#Librairie pour l'écran LCD.
from lcd1602 import LCD1602
#Librairie pour le temps.
from utime import sleep

#Déclaration des Pins et variables
#Capteur de lumière pin ADC(0)
PIR = Pin(18, Pin.IN)
#Configuration des Pins en utilisant le protocole I2C
#On choisit l'index 1, pour la synchronisation la pin 7, pour les données la pin 6 et une fréquence de 400000Hz
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000) 
#On définit l'écran LCD
#Le type de données, le nombre de rangées et le nombre de colonnes.
screen = LCD1602(i2c, 2, 16) 

#On affiche l'écran
screen.display()

#Boucle de lecture
while True:
    if PIR.value() == 1:
        screen.display()
        #On écrit "Welcome Home !" sur l'écran LCD.
        screen.print('Welcome Home !')
        #On remet le curseur au tout début
        screen.setCursor(0, 0)
    else:
        #On efface ce qui est écrit sur l'écran
        screen.clear()
    #On fait une pause de 2 secondes
    sleep(2)
    
        