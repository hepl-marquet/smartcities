#15/02/23 vincent.marquet@student.hepl.be
#PWM_LED_FADE.py
#Ce programme fait baisser/augmenter la luminosité de la LED progressivement

#Importation des librairies
import utime
from machine import Pin,PWM

#Déclaration relatives à la LED
LED_PWM=PWM(Pin(18))			#Pin utilisée pour la LED
LED_PWM.freq(500) 				#Fréquence de la LED

val=0
while True:
    while val<65535:			#Boucle pour augmenter l'intensité
        val=val+50				#Augmentation de l'intensité
        utime.sleep_ms(1)   
        LED_PWM.duty_u16(val)	#Mise à jour de l'intensité
    while val>0:				#Boucle pour diminuer l'intensité
        val=val-50				#Diminution de l'intensité
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)	#Mise à jour de l'intensité