![test2](https://raw.githubusercontent.com/hepl-marquet/smartcities/main/smartcities1.png)

Dans le cadre du cours de Projet Smartcities, nous allons à l'aide du Raspberry Pi Pico W pouvoir controller différents objets du Smart Corridor.
Afin de développer nos compétences et de nous préparer à cela, nous sommes amenés à réaliser différents exercices :

- [GPIO](GPIO) : LED simple, bouton-poussoir, interruption.
- [AD-PWM](AD-PWM) : Lecture du potentiomètre, PWM (LED, musique, servo).
- [LCD](LCD) : Documentation des fonctions de la librairie, affichage de la valeur du potentiomètre.
- [LED_neo](LED_neo) : utilisation des LEDs néopixel, documentation des fonctions de la librairie, arc-en-ciel.
- [Sensors](Sensors) : Température et humidité, luminosité, PIR.
- [Network](Network) : Accès réseau avec le RPi Pico.

![test](https://raw.githubusercontent.com/hepl-marquet/smartcities/main/testgithub.png)

## Le Raspberry Pi Pico W

![image](https://user-images.githubusercontent.com/124889426/217868716-ea079240-9f27-4855-9209-1cfc36a843a4.png)

Ci-dessus une image représentant les différentes connexions possibles du RPi Pico W, on dispose notamment de :

- 30 GPIOs dont 4 qui peuvent être utilisées en tant que ADC, 26 des 30 pins sont utilisables, dont 3 ADCs.
- Un port Micro USB.
- Un processeur 32bits Dual-core Arm Cortex M0+ avec une clock allant jusque 133MHz
- 246kB de SRAM et 2MB de mémoire Flash
- Un module Wi-Fi (802.11n)

Pour utiliser différents modules préfabriqués, nous utilisons un shield Grove, qui permet directement de connecter les différents modules.

Afin de communiquer avec le RPi Pico W nous devons utiliser un environnement et un langage, j'ai choisi Thonny comme environnement et j'utiliserai le langage micropython.

Thonny est un environnement simple et qui est compatible avec le RPi Pico W, pour pouvoir se connecter il faut aller dans Outils>Option>Interpréteur sélectionner MicroPython (Rapsberry Pi Pico).

Il est ensuite nécessaire de Booter le langage micropython dans le RPi Pico W, pour cela il faut brancher le Rpi en maintenant le bouton poussoir enfoncé, ainsi nous avons accès au Boot du RPi, ensuite il y a un lien dans le dossier qui permet de télécharger le langage micropython, il ne reste plus qu'à déposer l'instalateur dans le dossier du RPi.

Une fois tout cela fait et que l'on est bien connecté au RPi via Thonny, il ne reste plus qu'à insérer notre code dans le RPi.
