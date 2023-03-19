![Introduction](https://user-images.githubusercontent.com/124889426/224516611-bf5abe71-4ac2-4c32-b8ba-995c072dffa6.png)

Dans cette partie, Nous verrons le fonctionnement de l'écran LCD, le protocol I2C, la librairie lcd1602 et nous apprendrons à utiliser le module GROVE suivant :

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

## La librairie lcd1602 :

Pour utiliser ce module nous aurons besoin de la librairie lcd1602 qui est fournie avec le [guide]( https://files.seeedstudio.com/wiki/Grove_Shield_for_Pi_Pico_V1.0/Begiinner's-Guide-for-Raspberry-Pi-Pico.pdf) qui nous a été mis à disposition en suivant [ce lien]( https://github.com/TinkerGen/Pico-micropython).
Cette librairie n’étant pas implémentée par défaut dans thonny, contrairement aux autres libraires que nous avions déjà utilisées (utime, machine), il faut que l’on sauvegarde cette librairie dans notre Raspberry Pi Pico W pour pouvoir l’utiliser, pour cela rien de plus simple :

Tout en étant connecté à notre RPi, on ouvre notre librairie en l’occurrence : « lcd1602.py », ensuite on va dans « Fichier », « Enregistrer sous… », ensuite une petite fenêtre devrait s’ouvrir, on sélectionne « Raspberry Pi Pico » et puis on termine en cliquant sur « OK ». Vous venez d’enregistrer une librairie sur votre RPi et elle est maintenant directement utilisable en l’important dans votre code comme vous le faisiez pour les autres librairies.

### Les différentes fonctions présentes dans cette librairie sont :

```display()```
Active l’affichage

```no_display()```
Désactive l’affichage

```clear()```
Efface ce qui est écrit et remet le curseur au tout début.

```setCursor(col, row)```
Permet de déplacer le curseur à un endroit précis, elle prend deux paramètres :

  -	Col pour la colonne
  -	Row pour la rangée
  
```print(text)```
Affiche les caractères que nous avons écrit en paramètre.

```home()```
Permet de remettre le curseur à la position 0

```cursor()```
Affiche le curseur

```no_cursor()```
Cache le curseur

```blink()```
Fait clignoter le curseur

```no_blink()```
Arrete de faire cligonter le curseur

```autoscroll()```
Fait déplacer le texte automatiquement

```no_autoscroll()```
Arrete de déplacer le texte automatiquemenent

```create_char()```
Permet de créer un caractère

```command()```
Envoie la commande au LCD

```write()```
Permet d'écrire un caractère spécial à l'aide de [cette table](https://www.waveshare.com/datasheet/LCD_en_PDF/LCD1602.pdf) page 14.

![LesDiffCodes](https://user-images.githubusercontent.com/124889426/224516616-8f99617f-5f48-4130-a1fd-424198b55f48.png)

## [LCD_BASICS](LCD_BASICS.py)
- Programme qui permet d'afficher un message sur l'écran LCD

```
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
```

![Hello](https://user-images.githubusercontent.com/124889426/226183742-a7f32bf6-b1c6-4d34-9b06-b6495b97c8b4.jpg)

## [LCD_POTENTIOMETER_ANGLE](LCD_POTENTIOMETER_ANGLE.py)
- Programme qui affiche en degrés du Potentiomètre.

```
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
```

https://user-images.githubusercontent.com/124889426/226183720-d30e2a1e-c32a-45d6-9ded-114a92a69586.mp4
