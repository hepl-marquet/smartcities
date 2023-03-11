## AD-PWM

Le RPI Pico dispose d'un ADC permettant de passer d'un signal analogique à un signal digital cependant il ne dispose pas d'un DAC qui permettrait de passer d'un signal digital vers un signal analogique, hors, le controle de la luminosité d'une LED se fait via un signal analogique, la librairie PWM nous permet d'envoyer des signaux sous formes d'impulsions qui nous donne la possibilité de simuler des signaux sinusoidaux.

Nous apprendrons donc à utiliser la librairie PWM ainsi que les modules GROVE suivants :

- [Rotary Angle Sensor](https://wiki.seeedstudio.com/Grove-Rotary_Angle_Sensor/)
- [LED Socket Kit](https://wiki.seeedstudio.com/Grove-LED_Socket_Kit/)
- [Passive Buzzer (Bonus)](https://wiki.seeedstudio.com/Grove_passive_Buzzer/)
- [Servo (Bonus)](https://wiki.seeedstudio.com/Grove-Servo/)

## Les différents codes

  - [AD_POTENTIOMETER_BASICS](AD_POTENTIOMETER_BASICS.py)
      - Programme qui permet d'afficher la valeur lue par la pin liée au potentiomètre.
      - On apprend comment configurer une PIN en mode entrée et à lire son entrée.

```
#Importation des librairies
from machine import ADC
from utime import sleep

#Déclaration de la Pin
Potentiometre = ADC(0)              #Potentiomètre : PIN A0

#Boucle de lecture
while True:
    print(Potentiometre.read_u16()) #Affiche la valeur du potentiomètre
    sleep(1)                        #Pause de 1 seconde
```

  - [AD_POTENTIOMETER_LED](AD_POTENTIOMETER_LED.py)
      - Programme qui permet de controller la LED à partir de la valeur du potentiomètre.
      - On lit la donnée du potentiomètre et en fonction de sa valeur avec des conditions if, on peut allumer et éteindre la LED.

```
#Importation des librairies
from machine import ADC,Pin
from utime import sleep

#Déclaration des Pins
Potentiometre = ADC(0)                    #Potentiomètre : PIN A0
LED = Pin(16,Pin.OUT)                     #LED : PIN D16

#Boucle de lecture
while True:
    print(Potentiometre.read_u16())       #Affiche la valeur du potentiomètre
    if Potentiometre.read_u16() > 30000:  #Condition pour allumer la LED : valeur du potentiomètre supérieure à 30000
        LED.value(1)
        sleep(1)
    else:
        LED.value(0)
        sleep(1)
```

  - [PWM_POTENTIOMETER_LED](PWM_POTENTIOMETER_LED.py)
      - Programme qui permet de controller la luminosité d'une LED à l'aide du potentiomètre.
      - On apprend à utiliser les commandes de bases de la librairie PWM.

```
#Importation des librairies
from machine import Pin,ADC,PWM

#Déclaration de la Pin
Potentiometre = ADC(0)                            #Potentiomètre : PIN A0
LED_PWM = PWM(Pin(18))                            #LED : PIN D18
LED_PWM.freq(500)                                 #Frequence de la LED

#Boucle de lecture
while True:
    LED_PWM.duty_u16(Potentiometre.read_u16() )   #Variation du duty cycle, cela correspond à la période pendant laquelle l'impulsion est positive par rapport à la période total d'un cycle, et on controle le duty cyvle avec la valeur du potentiomètre qui est déjà ajusté avec la range de la LED
```

  - [BUZZER_SING](BUZZER_SING.py)
      - Programme qui joue la mélodie "Frères Jacques" à l'aide d'un passive buzzer connecté à la pin A1
      - 

```
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
```

  - [PWM_LED_FADE](PWM_LED_FADE.py)
      - Programme qui fait progressivement augmenter et diminuer l'intensité d'une LED.
      - Utilisation d'une boucle while qui fait grandir/diminuer progressivement une valeur.

```
#Importation des librairies
import utime
from machine import Pin,PWM

#Déclaration relatives à la LED
LED_PWM=PWM(Pin(18))          #Pin utilisée pour la LED
LED_PWM.freq(500)             #Fréquence de la LED

val=0
while True:
    while val<65535:		    	#Boucle pour augmenter l'intensité
        val=val+50			    	#Augmentation de l'intensité
        utime.sleep_ms(1)   
        LED_PWM.duty_u16(val)	#Mise à jour de l'intensité
    while val>0:			      	#Boucle pour diminuer l'intensité
        val=val-50			    	#Diminution de l'intensité
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)	#Mise à jour de l'intensité
```

  - [BONUS_BUZZER_POTENTIOMETER](BONUS_BUZZER_POTENTIOMETER.py)
      - Programme qui permet de controller la fréquence du son que sort le buzzer à l'aide du potentiomètre.

```
#Importation des librairies
from machine import ADC,Pin,PWM
from utime import sleep

#Déclaration des Pins et variables
ROTARY_ANGLE_SENSOR = ADC(0)				#Potentiomètre : PIN A0
buzzer = PWM(Pin(27))						#Buzzer :        PIN A1
Pot = 0

#Boucle de lecture
while True:
    print(ROTARY_ANGLE_SENSOR.read_u16()) 	#Affiche la valeur du potentiomètre
    Pot = ROTARY_ANGLE_SENSOR.read_u16()		#Insère la valeur dans la variable "a"
    buzzer.duty_u16(500)				          	#Volume du buzzer
    if 5000 >= Pot and Pot >= 0:				    #Différentes notes attribués à certaines valeurs obtenues par le potentiomètre.
        buzzer.freq(261)				          	#DO
    elif 10000 >= Pot and Pot >= 5000:
        buzzer.freq(293)				          	#RE
    elif 15000 >= Pot and Pot >= 10000:
        buzzer.freq(329)					          #MI
    elif 20000 >= Pot and Pot >= 15000:
        buzzer.freq(349)				          	#FA
    elif 25000 >= Pot and Pot >= 20000:
        buzzer.freq(392)				          	#SOL
    elif 30000 >= Pot and Pot >= 25000:
        buzzer.freq(440)					          #LA
    elif 35000 >= Pot and Pot >= 30000:
        buzzer.freq(493)					          #SI
    sleep(0.5)								              #Temps de lecture de la note
```

  - [BONUS_SERVO_POTENTIOMETER](BONUS_SERVO_POTENTIOMETER.py)
      - Programme qui permet de controller l'angle du servo moteur à l'aide du potentiomètre.

```
#Importation des librairies
from machine import Pin,ADC,PWM
from utime import sleep

#Déclaration des Pins
Angle_Sensor = ADC(0)
pwm_servo = PWM(Pin(20))

#Variable declaration
B = 0																        #Cette variable est utilisée pour vérifier si le potentiomètre a fort varié afin de ne faire tourner le moteur que lorsqu'il y a un "grand" changement sinon il se mettrait à jour en permanence et ce serait fort saccadé (>650)
pwm_servo.freq(100) 												#Fréquence du servo utilisé

#Main while loop
while True:
    A = Angle_Sensor.read_u16()										                #Deuxième mesure effectuée pour pouvoir vérifier la différence
    if abs(A-B) > 650:                                            #Condition pour que l'on change la position du moteur, au moins une différence de 650 entre les deux valeurs A et B
            Angle = int((Angle_Sensor.read_u16()/6.28) + 3250)		#Conversion de la valeur du potentiomètre vers une valeur convenable pour le servo
            print(Angle)											                    #Affichage de la valeur obtenue pour vérifier
            pwm_servo.duty_u16(Angle)								              #Déplacement du servo
            sleep(0.01)												                    #Petit délai pour ne pas actualiser trop vite
            B = Angle_Sensor.read_u16()								            #B prend la valeur précédente de l'angle pour pouvoir le comparrer à A
```
