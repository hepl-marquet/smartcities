![Introduction](https://user-images.githubusercontent.com/124889426/224517084-e3961c1f-b11f-4ded-9bd9-578b91154f08.png)

Voici les premiers exercices de µPython, ici nous apprenons les bases de ce langage et de l'utilisation du RPi Pico W ainsi que des modules GROVE : 

- [LED Socket Kit](https://wiki.seeedstudio.com/Grove-LED_Socket_Kit/)
- [Button](https://wiki.seeedstudio.com/Grove-Button/)

![LesDiffCodes](https://user-images.githubusercontent.com/124889426/224517141-fdb65e38-86f6-47dd-8548-8f84ecb85bb1.png)

## Quelques Commandes :

### PIN
Permet de configurer une PIN soit en sortie soit en entrée, ce qui est nécessaire lorsqu'on veut connecter un module par exemple.

### toggle()
Permet de passer de ON à OFF et vice-versa.

### value()
Permet de définir la valeur d'une sortie, 1 signifie ON et 0 signifie OFF ou de "lire" la valeur d'une entrée pour pouvoir la mettre dans une variable par exemple.

## [LED_BASICS](LED_BASICS.py)
- Programme qui allume ou éteint une LED connectée au port 16.
- Ce code envoie une valeur 1 (ou 0, il suffit de modifier cela dans le code) à la pin connectée à la LED, ce qui a pour effet de l'allumer (ou l'éteindre)

```
#Importation de la librairie
import machine

#Définition de la Pin et de son utilisation
LED = machine.Pin(16,machine.Pin.OUT)

#Si on met la valeur à 1, la LED s'allume si on met la valeur à 0, elle s'éteint.
LED.value(0)
```

![LedOn](https://user-images.githubusercontent.com/124889426/224517197-2072d76a-eb61-49e6-8f80-d40cabbf9fe8.jpg)

## [LED_BLINK_FOR](LED_BLINK_FOR.py)
- Programme qui fait clignoter une LED connectée au port 16 à 10 reprises.
- On utilise ici une boucle FOR qui allume puis éteint la LED et ce, à 10 reprises.
- On découvre l'utilisation de la librairie utime qui permet de mettre des delais dans le code avec notamment la commande sleep().

```
#Importation de la librairie principale
import machine
#Importation de la librairie du temps
import utime

#Définition de la Pin et de son utilisation
LED = machine.Pin(16,machine.Pin.OUT)

#Boucle FOR qui sera parcourue 10 fois
for i in range(10):
    #Allume la LED
    LED.value(1)
    #Fait une pause pendant 1 seconde
    utime.sleep(1)
    #Éteint la LED
    LED.value(0)
    #Fait une pause pendant 1 seconde
    utime.sleep(1)
```

## [LED_BLINK_WHILE](LED_BLINK_WHILE.py)
- Programme qui fait clignoter une LED connectée au port 16 indéfiniment.
- On crée une boucle WHILE qui fait clignoter la LED indéfiniment.

```
#Importation de la librairie principale
import machine
#Importation de la librairie du temps
import utime

#Définition de la Pin et de son utilisation
LED = machine.Pin(16,machine.Pin.OUT)

#Boucle WHILE infinie
while True:
    #Allume la LED
    LED.value(1)
    #Fait une pause pendant 1 seconde
    utime.sleep(1)
    #Éteint la LED
    LED.value(0)
    #Fait une pause pendant 1 seconde
    utime.sleep(1)
```

## [BUTTON_BASICS](BUTTON_BASICS.py)
- Programme qui permet d'allumer/éteindre une LED à l'aide d'un bouton poussoir.
- Nous apprennons ici la lecture d'une entrée et comment l'utiliser pour la renvoyer en sortie.
- Il faut tout d'abord configurer la pin que l'on souhaite lire comme une entrée.
- Ensuite à l'aide de la commande value() on peut "lire" la donnée et l'insérer dans une variable qui nous permet de créer une condition afin d'allumer ou non la LED.

```
#Importation de la librairie principale
import machine

#Définition des Pins et de leurs utilisations
LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)

#Boucle WHILE qui vérifie si l'on appuie sur le bouton
while True:
    #Valeur du bouton
    BUTTON_VAL = BUTTON.value()
    #Cas si on appuie sur le bouton
    if BUTTON_VAL == 1:
        #Allume la LED
        LED.value(1)
    #Cas si on appuie pas sur le bouton
    elif BUTTON_VAL == 0:
        #Éteint la LED
        LED.value(0)
```

![LedButton](https://user-images.githubusercontent.com/124889426/224517214-380e881e-09ed-4c53-95c6-a108620f4161.jpg)

![LedButtonON](https://user-images.githubusercontent.com/124889426/224517217-b1267f5e-62f6-417d-acff-b409ea836bb9.jpg)

## [BUTTON_LIGHT](BUTTON_LIGHT.py)
- Programme qui permet d'allumer/éteindre une LED à l'aide d'un bouton poussoir de la même manière qu'un interrupteur de la vie quotidienne.
- À l'aide de la commande toggle() et de ce qu'on appelle un FLAG, on peut simuler un intérrupteur que l'on peut retrouver chez soi.
- On commence par lire la donnée du bouton avec une boucle WHILE.
- Si elle est positive alors on incrémente le FLAG de 1, à partir de là on crée une condition pour allumer la LED, et une deuxième si le FLAG atteint la valeur de 2, on le réinitialise et on éteint la LED.

```
#Importation des librairies principale
from machine import Pin
from utime import sleep

#Définition des Pins et de leurs utilisations
LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)

#Initialisation du FLAG
LED_FLAG = 0

#Boucle WHILE qui vérifie si l'on appuie sur le bouton
while True:
   if BUTTON.value() == 1:
       #Incrémentation du FLAG
       LED_FLAG = LED_FLAG + 1
       #Pause de 0,3s (nécessaire sinon à l'appui du bouton, on recevrait plusieurs appuis d'un coup dû à la rapidité de lecture de la boucle)
       sleep(0.3)
       #Premier cas du FLAG (Allumer)
       if LED_FLAG == 1:
           LED.value(1)
       #Second cas du FLAG (Éteindre)
       elif LED_FLAG == 2:
           #Réinitialise le FLAG
           LED_FLAG = 0
           LED.value(0)
```

![LedButtonToggle](https://user-images.githubusercontent.com/124889426/224517221-535ef0f5-688a-4bd9-8200-4b0307f65632.jpg)
