#27/04/23 vincent.marquet@student.hepl.be
#NEO_BASICS.py
#Programme qui permet d'afficher et de faire défiler des couleurs sur la LED neopixels de plusieurs manières différentes.

#Importation des librairies
from ws2812 import WS2812
#Librairie utilisée pour la LED Neopixel
import time
#Librairie pour les delais

#Création de couleurs selon la norme RGB (Red, Green, Blue).
#Les variables créées ici sont des tuples qui contiennent 3 informations la valeur rouge, verte et bleue.
RED = (255, 0, 0)
ORANGE = (255, 255, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (100, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (WHITE, RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, PURPLE)

#Déclaration de la pin pour la LED.
led = WS2812(18,1)

#Première manière de faire défiler les couleurs, avec l'aide d'une boucle for et de la commande "pixels_fill()".
print("fills")
for color in COLORS:
    led.pixels_fill(color)
    led.pixels_show()
    time.sleep(0.2)

#Deuxième manière de faire défiler les couleurs, à l'aide de la commande "color_chase()"
print("chases")
for color in COLORS:
    led.color_chase(color, 0.01)

#Commande qui permet de faire défiler les couleurs de l'arc-en-ciel en 
print("rainbow")
led.rainbow_cycle(0)