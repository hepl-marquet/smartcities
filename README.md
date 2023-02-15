## Le Projet Smartcities

Dans le cadre du cours de Projet Smartcities, nous allons à l'aide du Raspberry Pi Pico W pouvoir controller différentes objets du Smart Corridor.

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

[GPIO](GPIO)
