![Introduction](https://user-images.githubusercontent.com/124889426/224516611-bf5abe71-4ac2-4c32-b8ba-995c072dffa6.png)

Dans cette partie, nous apprendrons à utiliser le protocol I2C ainsi que le module GROVE suivant :

- [16x2 LCD Screen](https://wiki.seeedstudio.com/Grove-16x2_LCD_Series/#docusaurus_skipToContent_fallback)

## LCD

Les écrans LCD (Liquid Crystal Display) sont une technologie d'affichage numérique qui utilise des cristaux liquides pour produire des images sur un écran plat les cristaux liquides sont situés entre deux feuilles de verre polarisant ces derniers peuvent se tordre ou s'aligner en fonction de la tension électrique appliquée. Lorsqu'une tension électrique est appliquée à une région spécifique de l'écran LCD, les cristaux liquides dans cette région s'alignent pour permettre ou bloquer la lumière polarisée qui traverse l'écran. Cela crée des pixels lumineux ou sombres sur l'écran.
Les cristaux liquides en eux-mêmes ne sont pas suffisant pour faire un affichage, en effet ils ne produisent pas de lumière mais permettent simplement de la bloquer ou de la laisser passer, c’est pourquoi il faut en combinaison de ceux-ci une source de lumière.
Le module Grove que nous utilisons s’appelle : 16 x 2 LCD Module, ce qui signifie qu’il permet d’afficher 16 caractères par ligne et 2 lignes donc un total de 32 caractères.

## I2C

Pour pouvoir communiquer avec notre écran LCD nous avons besoin du protocole I2C, c’est un protocole simple : il utilise deux fils pour la communication : un fil de données (SDA) et un fil d'horloge (SCL). Le fil de données est bidirectionnel et est utilisé pour transmettre les données entre les composants, tandis que le fil d'horloge est unidirectionnel et est utilisé pour synchroniser la communication entre les composants.
Afin de définir la pin I2C il faut utiliser la commande : 

```machine.I2C(id,*,scl,sda,freq)```

cette commande prend en paramètres :

-	id : elle identifie le périphérique I2C spécifique, et dépend de l’endroit sur le shield grove.
-	scl : pin qui sera utilisée pour synchroniser avec la clock.
-	sda : pin qui sera utilisée pour transférer les données.
-	freq : c’est la fréquence maximale qui sera utilisée pour la communication et dépend du module que nous utiliserons.


![LesDiffCodes](https://user-images.githubusercontent.com/124889426/224516616-8f99617f-5f48-4130-a1fd-424198b55f48.png)

## La librairie lcd1602 :

Pour utiliser ce module nous aurons besoin de la librairie lcd1602 qui est fournie avec le [guide]( https://files.seeedstudio.com/wiki/Grove_Shield_for_Pi_Pico_V1.0/Begiinner's-Guide-for-Raspberry-Pi-Pico.pdf) qui nous a été mis à disposition en suivant [ce lien]( https://github.com/TinkerGen/Pico-micropython).
Cette librairie n’étant pas implémentée par défaut dans thonny, contrairement aux autres libraires que nous avions déjà utilisées (utime, machine), il faut que l’on sauvegarde cette librairie dans notre Raspberry Pi Pico W pour pouvoir l’utiliser, pour cela rien de plus simple :
Tout en étant connecté à notre RPi, on ouvre notre librairie en l’occurrence : « lcd1602.py », ensuite on va dans « Fichier », « Enregistrer sous… », ensuite une petite fenêtre devrait s’ouvrir, on sélectionne « Raspberry Pi Pico » et puis on termine en cliquant sur « OK ». Vous venez d’enregistrer une librairie sur votre RPi et elle est maintenant directement utilisable en l’important dans votre code comme vous le faisiez pour les autres librairies.
Les différentes fonctions présentent dans cette librairie sont :

###display()

Elle active l’affichage

###no_display()

Elle désactive l’affichage

###clear()

Elle efface ce qui est écrit et remet le curseur au tout début.

###setCursor(col, row)

Elle permet de déplacer le curseur à un endroit précis, elle prend deux paramètres :

  -	Col pour la colonne
  -	Row pour la rangée
  
###print(text)

Elle affiche les caractères que nous avons écrit en paramètre.

## [LCD_BASICS](LCD_BASICS.py)
- Programme qui permet d'afficher la valeur lue par la pin liée au potentiomètre.
- On voit que pour lire la valeur du potentiomètre nous avons utilisé un ADC.
- Il faut également se servir de la commande read_u16 pour pouvoir lire la donnée.

```
#Importation des librairies
from machine import ADC
from utime import sleep

#Déclaration de la Pin
#Potentiomètre : PIN A0
Potentiometre = ADC(0)

#Boucle de lecture
while True:
    #Affiche la valeur du potentiomètre
    print(Potentiometre.read_u16())
    #Pause de 1 seconde
    sleep(1)                        
```

![Potentio](https://user-images.githubusercontent.com/124889426/224516955-94f55e6e-70ab-4590-90ce-424c1e930fe0.jpg)

![Console](https://user-images.githubusercontent.com/124889426/224517692-fc6e93a6-f567-4516-a99c-ddcaaba63c91.png)


## [AD_POTENTIOMETER_LED](AD_POTENTIOMETER_LED.py)
- Programme qui permet de controller la LED à partir de la valeur du potentiomètre.
- On lit la donnée du potentiomètre et en fonction de sa valeur avec des conditions if, on peut allumer et éteindre la LED.

```
#Importation des librairies
from machine import ADC,Pin
from utime import sleep

#Déclaration des Pins
#Potentiomètre : PIN A0
Potentiometre = ADC(0)
#LED : PIN D16
LED = Pin(16,Pin.OUT)

#Boucle de lecture
while True:
    #Affiche la valeur du potentiomètre
    print(Potentiometre.read_u16())
    #Condition pour allumer la LED : valeur du potentiomètre supérieure à 30000
    if Potentiometre.read_u16() > 30000: 
        LED.value(1)
        sleep(1)
    else:
        LED.value(0)
        sleep(1)
```


https://user-images.githubusercontent.com/124889426/224517018-c3c433d0-7e1b-4cff-a88c-e118667bdc08.mp4


## [PWM_POTENTIOMETER_LED](PWM_POTENTIOMETER_LED.py)
- Programme qui permet de controller la luminosité d'une LED à l'aide du potentiomètre.
- On commence par lire la valeur du potentiomètre à l'aide de l'ADC.
- On crée un signal PWM de sortie vers la LED.
- On modifie la valeur de ce signal à partir de la valeur lue au potentiomètre (Dans certains cas il faut adapter les extrémités des valeurs ensemble, il y a un exemple plus bas avec le servo moteur)

```
#Importation des librairies
from machine import Pin,ADC,PWM

#Déclaration de la Pin
#Potentiomètre : PIN A0
Potentiometre = ADC(0)
#LED : PIN D18
LED_PWM = PWM(Pin(18))
#Frequence de la LED
LED_PWM.freq(500)

#Boucle de lecture
while True:
    #Variation du duty cycle, cela correspond à la période pendant laquelle l'impulsion est positive par rapport à la période total d'un cycle, et on controle le duty cyvle avec la valeur du potentiomètre qui est déjà ajusté avec la range de la LED
    LED_PWM.duty_u16(Potentiometre.read_u16())
```


https://user-images.githubusercontent.com/124889426/224517029-f45491f8-98ab-4d90-8a5d-fe3cd2c12969.mp4


## [BUZZER_SING](BUZZER_SING.py)
- Programme qui joue la mélodie "Frères Jacques" à l'aide d'un passive buzzer connecté à la pin A1
- On définit un signal PWM sortant vers le buzzer.
- On choisit un volume.
- On crée des définitions pour chaques notes contenant :
  - La commande pour faire jouer la note au buzzer
  - La commande pour définir la fréquence de la note
  - La durée de la note
  - À partir de la partition, on peut ensuite recréer la musique souhaitée en oubliant pas de mettre en paramètre, lors de l'appel à la fonction, la durée de la note en secondes.

```
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

![Buzzer](https://user-images.githubusercontent.com/124889426/224517057-d88c9429-36e4-484e-ab87-c807c7dbd1ff.jpg)


## [PWM_LED_FADE](PWM_LED_FADE.py)
- Programme qui fait progressivement augmenter et diminuer l'intensité d'une LED.
- On définit un signal PWM pour la pin de la LED.
- On crée une boucle qui va faire varier le duty cycle du signal PWM.

```
#Importation des librairies
import utime
from machine import Pin,PWM

#Déclaration relatives à la LED
#Pin utilisée pour la LED
LED_PWM=PWM(Pin(18))
#Fréquence de la LED
LED_PWM.freq(500)

val=0
while True:
    #Boucle pour augmenter l'intensité
    while val<65535:
        #Augmentation de l'intensité
        val=val+50
        utime.sleep_ms(1)
        #Mise à jour de l'intensité
        LED_PWM.duty_u16(val)
    #Boucle pour diminuer l'intensité
    while val>0:
        #Diminution de l'intensité
        val=val-50
        utime.sleep_ms(1)
        #Mise à jour de l'intensité
        LED_PWM.duty_u16(val)
```

## [BONUS_BUZZER_POTENTIOMETER](BONUS_BUZZER_POTENTIOMETER.py)
- Programme qui permet de controller la fréquence du son que sort le buzzer à l'aide du potentiomètre.
- On lit la valeur du potentiomètre.
- On crée plusieurs conditions dans la range du potentiomètre pour définir des intervalles dans lesquelles les différentes notes sont jouées

```
#Importation des librairies
from machine import ADC,Pin,PWM
from utime import sleep

#Déclaration des Pins et variables
#Potentiomètre : PIN A0
ROTARY_ANGLE_SENSOR = ADC(0)
#Buzzer : PIN A1
buzzer = PWM(Pin(27))
Pot = 0

#Boucle de lecture
while True:
    #Affiche la valeur du potentiomètre
    print(ROTARY_ANGLE_SENSOR.read_u16())
    #Insère la valeur dans la variable "a"
    Pot = ROTARY_ANGLE_SENSOR.read_u16()
    #Volume du buzzer
    buzzer.duty_u16(500)
    #Différentes notes attribués à certaines valeurs obtenues par le potentiomètre.
    if 5000 >= Pot and Pot >= 0:
        #DO
        buzzer.freq(261)
    elif 10000 >= Pot and Pot >= 5000:
        #RE
        buzzer.freq(293)
    elif 15000 >= Pot and Pot >= 10000:
        #MI
        buzzer.freq(329)
    elif 20000 >= Pot and Pot >= 15000:
        #FA
        buzzer.freq(349)
    elif 25000 >= Pot and Pot >= 20000:
        #SOL
        buzzer.freq(392)
    elif 30000 >= Pot and Pot >= 25000:
        #LA
        buzzer.freq(440)
    elif 35000 >= Pot and Pot >= 30000:
        #SI
        buzzer.freq(493)
    #Temps de lecture de la note
    sleep(0.5)
```

## [BONUS_SERVO_POTENTIOMETER](BONUS_SERVO_POTENTIOMETER.py)
- Programme qui permet de controller l'angle du servo moteur à l'aide du potentiomètre.
- On lit la valeur du potentiomètre.
- On l'adapte à la range de fonctionnement du servo.
- On envoie la valeur au servo.

```
#Importation des librairies
from machine import Pin,ADC,PWM
from utime import sleep

#Déclaration des Pins
Angle_Sensor = ADC(0)
pwm_servo = PWM(Pin(20))

#Variable declaration
#Cette variable est utilisée pour vérifier si le potentiomètre a fort varié afin de ne faire tourner le moteur que lorsqu'il y a un "grand" changement sinon il se mettrait à jour en permanence et ce serait fort saccadé (>650)
B = 0
#Fréquence du servo utilisé
pwm_servo.freq(100)

#Main while loop
while True:
    #Deuxième mesure effectuée pour pouvoir vérifier la différence
    A = Angle_Sensor.read_u16()
    #Condition pour que l'on change la position du moteur, au moins une différence de 650 entre les deux valeurs A et B
    if abs(A-B) > 650:
            #Conversion de la valeur du potentiomètre vers une valeur convenable pour le servo
            Angle = int((Angle_Sensor.read_u16()/6.28) + 3250)
            #Affichage de la valeur obtenue pour vérifier
            print(Angle)
            #Déplacement du servo
            pwm_servo.duty_u16(Angle)
            #Petit dé
