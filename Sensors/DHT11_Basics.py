#06/04/23 vincent.marquet@student.hepl.be
#DHT11_Basics.py
#Programme qui permet de lire la température et l'humidité ambiante.

#Importation des librairies.
from dht11 import *         #Librairie pour le capteur DHT.
from machine import Pin     #Librairie pour la configuration des pins.
from utime import sleep     #Librairie pour le temps.

#On définit la pin du capteur DHT11.
dht = DHT(18)

#On crée une boucle de lecture qui va afficher les valeurs lues dans la console.
while True:
    #On lit les valeurs du capteur et on les met dans des variables "temp" et "humid".
    temp,humid = dht.readTempHumid()
    #Pause de 1 seconde.
    sleep(1)
    #Affichage de la température.
    print("Température :",temp)
    #Affichage de l'humidité.
    print("Humidité :",humid)