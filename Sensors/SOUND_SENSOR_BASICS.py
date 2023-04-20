#20/04/23 vincent.marquet@student.hepl.be
#SOUND_SENSOR_BASICS.py
#Programme qui permet d'afficher la valeur lue par le capteur de son.

#Importation des librairies
from machine import ADC

#Déclaration des Pins
SOUND_SENSOR = ADC(0)						#Capteur de son : PIN A0, range de 0-65535 soit 16bits

#Boucle de lecture
while True:
    #Affichage de la valeur lue par le capteur.
    print(SOUND_SENSOR.read_u16())
    
    
#     average = 0
#     for i in range (1000):
#         noise = SOUND_SENSOR.read_u16()
#         average += noise
#     noise = average/1000
#     print(noise)
#     LED_PWM.duty_u16(int(noise*5))	