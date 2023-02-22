#16/02/23 vincent.marquet@student.hepl.be
#AD_POTENTIOMETER_BASICS.py
#Programme qui permet d'afficher la valeur lue par la pin liée au potentiomètre.

#Importation des librairies
from machine import ADC
from utime import sleep

#Déclaration de la Pin
Potentiometre = ADC(0)						#Potentiomètre : PIN A0

#Boucle de lecture
while True:
    print(Potentiometre.read_u16()) 		#Affiche la valeur du potentiomètre
    sleep(1)								#Pause de 1 seconde