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

### HUMIDITY & TEMPERATURE SENSOR

[DHT11_BASICS](DHT11_Basics.py)

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

### SOUND SENSOR

[SOUND_SENSOR_BASICS](SOUND_SENSOR_BASICS.py)

- Programme qui permet d'afficher la lecture du capteur son.
- Le capteur de son a une range de 0 à 65535 dû à l'adc 16 bits.

```
#Importation des librairies
from machine import ADC

#Déclaration de la pin du capteur de son.
SOUND_SENSOR = ADC(0)

#Boucle de lecture
while True:
    #Affichage de la valeur lue par le capteur.
    print(SOUND_SENSOR.read_u16())
    
```

![image](https://user-images.githubusercontent.com/124889426/233376720-f6a0c6f0-cf79-4c3c-9075-4d1a6dda9fd8.png)

On observe une multitude de valeurs obtenues par le capteur de son notamment plusieurs 0 ce qui peut parfois être dérangeant, nous verrons dans le prochain code une manière de palier à cela.

[SOUND_SENSOR_AVERAGE](SOUND_SENSOR_AVERAGE.py)

- Programme qui permet d'afficher la lecture du capteur son.
- Le capteur de son a une range de 0 à 65535 dû à l'adc 16 bits.
- Étant donné que le capteur affiche parfois des 0, nous faisons une moyenne pour ne plus que cela se reproduise, on a ainsi une meilleur idée du volume sonore ambiant.

```
#Importation des librairies.
from machine import ADC

#Déclaration des Pins.
SOUND_SENSOR = ADC(0)						#Capteur de son : PIN A0, range de 0-65535 soit 16bits.

#Boucle de lecture.
while True:
    #Déclaration de la variable "average" qui sera la moyenne des mesures effectuées.
    average = 0
    #On crée une boucle for qui va s'effectuer 1000 fois.
    for i in range (1000):
        #On enregistre la valeur lue dans la variable "noise".
        noise = SOUND_SENSOR.read_u16()
        #On additione tous les échantillons.
        average += noise
    #Calcul de la moyenne.
    average = average/1000
    #Affichage de la moyenne.
    print(average)
    
```

![image](https://user-images.githubusercontent.com/124889426/233379034-073fca0f-15a9-4d19-827b-05a53f53573f.png)

Ci-dessus on observe que les valeurs ne sont plus égales à 0, en revanche elles sont désormais des float car ce sont des nombres à virgules, si l'on souhaitait exploité ces données pour quelque chose il faudrait potentiellement les retransformer en entier à l'aide de la commande :

```int()```

[SOUND_SENSOR_LED](SOUND_SENSOR_LED.py)

- Programme qui permet d'allumer plus ou  moins fort une LED en fonction du volume ambiant.

```
#Importation des librairies.
from machine import ADC, Pin, PWM

#Déclaration des Pins.
#Capteur de son : PIN A0, range de 0-65535 soit 16bits.
SOUND_SENSOR = ADC(0)
#LED : PIN D18
LED_PWM = PWM(Pin(18))
#Fréquence de la LED
LED_PWM.freq(500)


#Boucle de lecture.
while True:
    #Déclaration de la variable "average" qui sera la moyenne des mesures effectuées.
    average = 0
    #On crée une boucle for qui va s'effectuer 1000 fois.
    for i in range (1000):
        #On enregistre la valeur lue dans la variable "noise".
        noise = SOUND_SENSOR.read_u16()
        #On additione tous les échantillons.
        average += noise
    #Calcul de la moyenne.
    average = average/1000
    #On teste si la moyenne est à un certain barème et en fonction du barème, on allume plus ou moins fort la LED.
    if average <= 9000:
        LED_PWM.duty_u16(0)
    elif average > 9000 and average <= 12000:
        LED_PWM.duty_u16(15000)
    elif average > 12000:
        LED_PWM.duty_u16(65535)
```

https://user-images.githubusercontent.com/124889426/233386959-f42f22ea-0a71-4bf8-979f-38b1b75856e4.mp4

NB : Il est important de noter que je n'ai pas mit de delay ou autre dans ma boucle de lecture et il faut faire attention à ne pas faire tourner en boucle à une telle vitesse un grand nombre de capteurs au risque de faire crasher le CPU.

### LIGHT SENSOR

[LIGHT_SENSOR_BASICS](LIGHT_SENSOR_BASICS.py)

- Programme qui permet d'afficher la valeur lue par le capteur de luminosité.

```
#Importation des librairies
from machine import ADC
from utime import sleep

#Déclaration des Pins et variables
#Capteur de lumière pin ADC(0)
LIGHT_SENSOR = ADC(0)

#Boucle de lecture
while True:
    #Affiche la valeur lue par le capteur de luminosité.
    print(LIGHT_SENSOR.read_u16())
    sleep(1)
    
```

![image](https://user-images.githubusercontent.com/124889426/233390227-3d566af0-1b36-4a1e-91eb-71b235fddfeb.png)

[LIGHT_SENSOR_BUZZER](LIGHT_SENSOR_BUZZER.py)

- Programme qui permet de faire sonner le buzzer lorsque la lumière est allumée.

```
#Importation des librairies
from machine import ADC, PWM, Pin
from utime import sleep

#Déclaration des Pins et variables
#Capteur de lumière pin ADC(0)
LIGHT_SENSOR = ADC(0)
#Buzzer pin ADC(1)
Buzzer = PWM(Pin(27))
#Fréquence du buzzer
Buzzer.freq(1046)

#Boucle de lecture
while True:
    #On fait une condition pour voir si la lumière est allumée
    if LIGHT_SENSOR.read_u16() >= 25000:
        #On règle le volume du buzzer
        Buzzer.duty_u16(1000)
        #On fait sonner pendant 1 seconde
        sleep(1)
    #On coupe le volume
    Buzzer.duty_u16(0)
```

### PIR SENSOR

[PIR_SENSOR_BASICS](PIR_SENSOR_BASICS.py)

- Programme qui permet de détecter un mouvement et de le dire dans la console toutes les 8 secondes.

```
#Importation des librairies
from machine import Pin
from utime import sleep

#Déclaration des Pins et variables
#Capteur de lumière pin ADC(0)
PIR = Pin(18, Pin.IN)

#Boucle de lecture
while True:
    #On fait une condition pour voir si le capteur détecte un mouvement.
    if PIR.value() == 1:
        #On affiche "Mouvement détecté"
        print('Mouvement détecté')
    elif PIR.value() == 0:
        #On affiche "Pas de mouvement détecté"
        print('Pas de mouvement détecté')
    sleep(8)
```

![image](https://user-images.githubusercontent.com/124889426/233395868-48f03898-2a8c-4716-b729-5801711483fc.png)

[PIR_SENSOR_WELCOME](PIR_SENSOR_WELCOME.py)

- Programme qui détecte les mouvements et envoie un message d'accueil sur l'écran LCD.

```
#Importation des librairies.
from machine import Pin,I2C
#Librairie pour l'écran LCD.
from lcd1602 import LCD1602
#Librairie pour le temps.
from utime import sleep

#Déclaration des Pins et variables
#Capteur de lumière pin ADC(0)
PIR = Pin(18, Pin.IN)
#Configuration des Pins en utilisant le protocole I2C
#On choisit l'index 1, pour la synchronisation la pin 7, pour les données la pin 6 et une fréquence de 400000Hz
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000) 
#On définit l'écran LCD
#Le type de données, le nombre de rangées et le nombre de colonnes.
screen = LCD1602(i2c, 2, 16) 

#On affiche l'écran
screen.display()

#Boucle de lecture
while True:
    if PIR.value() == 1:
        screen.display()
        #On écrit "Welcome Home !" sur l'écran LCD.
        screen.print('Welcome Home !')
        #On remet le curseur au tout début
        screen.setCursor(0, 0)
    else:
        #On efface ce qui est écrit sur l'écran
        screen.clear()
    #On fait une pause de 2 secondes
    sleep(2)
```

https://user-images.githubusercontent.com/124889426/233402145-a5050e26-c2dd-487f-8b38-e31293f84771.mp4
