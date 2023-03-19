#19/03/23 vincent.marquet@student.hepl.be
#LCD_POTENTIOMETER_ANGLE.py
#Programme qui permet d'afficher l'angle du potentiomètre sur l'écran LCD.

#Importation des librairies
from lcd1602 import LCD1602 #Librairie pour l'écran LCD
from machine import I2C,Pin,ADC #Librairie pour la configuration des pins
from utime import sleep     #Librairie pour le temps

#Configuration des Pins en utilisant le protocole I2C
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000) #On choisit l'index 1, pour la synchronisation la pin 7, pour les données la pin 6 et une fréquence de 400000Hz
#On définit l'écran LCD
screen = LCD1602(i2c, 2, 16) #Le type de données, le nombre de rangées et le nombre de colonnes.
#Ajout du potentiomètre
Potentiometer = ADC(0)

while True :
    sleep(1) #On fait une pause d'une seconde
    screen.clear() #On efface l'écran et le curseur revient à la position initiale
    screen.print('Angle') #On affiche "Angle"
    screen.setCursor(0,2) #On déplace le curseur à la deuxième rangée
    screen.print(str(round(Potentiometer.read_u16()/65355*300-1))) #Affichage de l'angle, attention à bien transformer la donnée lue en string car la fonction print() du lcd ne prend que les string en paramètres. il faut également retransformer la valeur lue par l'adc en degrés grâce à cette formule : Valeur/65535*300, je fais -1 car je voulais arriver à un résultat compris entre [0,300], avec mon round() qui permet d'arrondir vers le haut ce n'était pas possible mais ainsi c'est réglé.
    screen.write(0b11011111) #On ajoute le symbole ° à la fin de la valeur