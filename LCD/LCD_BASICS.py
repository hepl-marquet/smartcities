#19/03/23 vincent.marquet@student.hepl.be
#LCD_BASICS.py
#Programme qui permet d'afficher un message sur un afficheur LCD.

#Importation des librairies
from lcd1602 import LCD1602 #Librairie pour l'écran LCD
from machine import I2C,Pin #Librairie pour la configuration des pins
from utime import sleep     #Librairie pour le temps

#Configuration des Pins en utilisant le protocole I2C
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000) #On choisit l'index 1, pour la synchronisation la pin 7, pour les données la pin 6 et une fréquence de 400000Hz
#On définit l'écran LCD
screen = LCD1602(i2c, 2, 16) #Le type de données, le nombre de rangées et le nombre de colonnes.

screen.display() #On affiche l'écran
screen.clear() #On efface ce qui était écrit
screen.print('Hello World') #On écrit "Hello World" (Ceci est à titre d'exemple, si l'on souhaite on peut modifier mais attention à ne pas dépasser le nombre de caractères sur la rangée.)
screen.setCursor(0, 2) #On déplace le curseur à la deuxième rangée
screen.print('By Marquet') #On écrit ce que l'on souhaite afficher.