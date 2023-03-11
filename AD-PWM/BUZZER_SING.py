#11/03/23 vincent.marquet@student.hepl.be
#BUZZER_SING.py
#Programme qui joue la mélodie "Frères Jacques" à l'aide d'un passive buzzer connecté à la pin A1

from machine import Pin,PWM
from utime import sleep

#Déclaration des Pins et variables
#Buzzer : PIN A1
buzzer = PWM(Pin(27))

#Choix du volume
vol = 500

#Définition des fonctions des différentes notes de musique
def DO(time):
    #Fait jouer la note au volume défini
    buzzer.duty_u16(vol)
    #Fréquence de la note
    buzzer.freq(1046)
    #Durée de la note
    sleep(time)
def RE(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1175)
    sleep(time)
def MI(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1318)
    sleep(time)
def FA(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1397)
    sleep(time)
def SOL(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1568)
    sleep(time)
def LA(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1760)
    sleep(time)
def SI(time):
    buzzer.duty_u16(vol)
    buzzer.freq(1967)
    sleep(time)
def N(time):
    buzzer.duty_u16(0)
    sleep(time)

#Boucle de lecture
while True:
    #Utilisation des notes définies
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    N(0.01)
        
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    
    MI(0.25)
    FA(0.25)
    SOL(0.5)
        
    MI(0.25)
    FA(0.25)
    SOL(0.5)
    N(0.01)

    SOL(0.125)
    LA(0.125)
    SOL(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    SOL(0.125)
    LA(0.125)
    SOL(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    RE(0.25)
    SOL(0.25)
    DO(0.5)
    N(0.01)
    
    RE(0.25)
    SOL(0.25)
    DO(0.5)