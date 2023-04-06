![image](https://user-images.githubusercontent.com/124889426/230333423-8adeddd6-d5fe-4f2d-a4d0-728cf1177dbc.png)

Les capteurs sont des dispositifs électroniques qui convertissent une grandeur physique, telle que la température, la pression, l'humidité, le son ou la lumière, en un signal électrique mesurable, ils sont ensuite traités à l'aide notamment d'un ADC (Analog to Digital Converter) qui permet de digitaliser ces signaux et ensuite de les utiliser dans nos codes.

- [Temperature&Humidity Sensor](https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/)
- [Sound Sensor](https://wiki.seeedstudio.com/Grove-Sound_Sensor/#docusaurus_skipToContent_fallback)
- [Light Sensor](https://wiki.seeedstudio.com/Grove-Light_Sensor/#docusaurus_skipToContent_fallback)
- [Mini Pir Motion Sensor](https://www.seeedstudio.com/Grove-mini-PIR-motion-sensor-p-2930.html)

## Temperature & Humidity Sensor

Nous utilisons ici un capteur DHT pour mesurer la température et l'humidité, les capteur DHT contiennent un élément résistif dont la résistance varie en fonction de la température et de l'humidité. Un circuit electronique permet ensuite de mesurer la variation de tension qui occure au sein du capteur lorsque la résistance varie.

## Sound Sensor

Le composant principal du capteur de son est un microphone, il est composé d'une capsule contenant une membrane mince qui vibre en réponse à l'onde sonore et d'un matériau piézoélectrique (Matériau qui transforme une énergie mécanique en énergie électrique), en combinant les deux on obtient un système qui crée un courant proportionnel à la pression accoustique.

## Light Sensor

Les capteurs de luminosité sont composés d'une photorésistance, dont la valeur varie en fonction de l'intensité lumineuse qu'on lui soumet, ainsi on peut mesurer la variation de tension qui occure au sein du capteur.

## Mini Pir Motion Sensor

Les capteurs PIR (Passive infrared) sont des capteurs de mouvement, ils se servent de matériaux pyroélectrique et des propriétés de l'infrarouge pour détecter un éventuel mouvement, ces matériaux générer de l'énergie lorsqu'ils sont exposés à un rayonnement infrarouge, ils sont généralement couplés à une lentille de Fresnel qui focalise les signaux infrarouge sur le capteur pyroélectrique, on peut ainsi obtenir un signal électrique à partir d'un mouvement.

![image](https://user-images.githubusercontent.com/124889426/230343354-06b4592c-f70e-4b84-87f5-0a704e9b1de1.png)

## [DHT11_BASICS](DHT11_Basics.py)

- Programme qui permet de lire la température et l'humidité ambiante.
- On utilise la librairie [dht11](https://github.com/TinkerGen/Pico-micropython/blob/master/dht11.py) qu'il faut préalablement enregistrer sur le RPi.

```
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
```

![image](https://user-images.githubusercontent.com/124889426/230345274-1d18e5b8-6a4d-480f-a1b9-890534b72dab.png)
