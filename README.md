![smartcities1](https://user-images.githubusercontent.com/124889426/224480242-2a5ed4d0-65ee-4352-a19a-042ea76c978a.png)

Dans le cadre du cours de Projet Smartcities, nous allons à l'aide du Raspberry Pi Pico W pouvoir controller différents objets du Smart Corridor.
Afin de développer nos compétences et de nous préparer à cela, nous sommes amenés à réaliser différents exercices :

- [GPIO](GPIO) : LED simple, bouton-poussoir, interruption.
- [AD-PWM](AD-PWM) : Lecture du potentiomètre, PWM (LED, musique, servo).
- [LCD](LCD) : Documentation des fonctions de la librairie, affichage de la valeur du potentiomètre.
- [LED_neo](LED_neo) : utilisation des LEDs néopixel, documentation des fonctions de la librairie, arc-en-ciel.
- [Sensors](Sensors) : Température et humidité, luminosité, PIR.
- [Network](Network) : Accès réseau avec le RPi Pico.

![RPi Pico](https://user-images.githubusercontent.com/124889426/224481824-08166b23-c766-46a1-8db5-2db9fc55c913.png)
![image](https://user-images.githubusercontent.com/124889426/217868716-ea079240-9f27-4855-9209-1cfc36a843a4.png)

Ci-dessus une image représentant les pins du RPi Pico W.

## Pins

- 40 x Pins
    -  26 x Pins utilisables
        -  3  x ADCs 12bits
        -  23 x GPIOs
        -  16 x PWM
        -  2  x I2C
        -  2  x SPI
        -  2  x UART

## Autres informations

- Un port Micro USB.
- Un processeur 32bits Dual-core Arm Cortex M0+ avec une clock allant jusque 133MHz
- 246kB de SRAM et 2MB de mémoire Flash
- Un module Wi-Fi (802.11n)

Afin de communiquer avec le RPi Pico W nous devons utiliser un environnement et un langage, j'ai choisi Thonny comme environnement et j'utiliserai le langage Micropython.

![MicroPython](https://user-images.githubusercontent.com/124889426/224481254-68c7bc6b-7572-4f3f-ad62-f6d775d1bed4.png)

MicroPython est une implémentation du langage de programmation Python conçue pour fonctionner sur des microcontrôleurs et des plates-formes embarquées à ressources limitées. MicroPython est utilisé dans beaucoup de projet de systèmes embarqués en raison de sa simplicité et sa flexibilité.

## Installation

Pour installer MicroPython sur le RPi Pico W il faut booter le langage dans le RPi, pour cela il faut se brancher à l'aide d'un cable USB tout en maintenant le bouton poussoir du RPi enfoncé, on aura ensuite accès aux fichiers de ce dernier, vous devriez y trouver un raccourci vers une page web appelé INDEX.html, cela vous redirigera directement vers le site pour télécharger une version de MicroPython, il faut suffira ensuite de télécharger la version souhaitée et de déposer l'installateur dans le répertoire du RPi qui se chargera du reste.

![Thonny](https://user-images.githubusercontent.com/124889426/224481630-174fba12-2a34-4edd-9fc5-f1627cf59e02.png)

Thonny est un IDE (environnement de développement intégré) pour python. Il présente l'avantage d'être facile d'accès pour les débutants et est compatible avec le RPi Pico W, pour pouvoir se connecter au RPi il suffit d'aller dans Outils>Option>Interpréteur, sélectionner MicroPython (Rapsberry Pi Pico). Une fois cela fait, le RPi est prêt à recevoir vos codes en MicroPython.

![Grove](https://user-images.githubusercontent.com/124889426/224482024-3f9c475f-385a-4d7d-a5f9-2b89fc40c02e.png)

La carte Grove est une carte d'extension conçue pour être utilisée avec le microcontrôleur Raspberry Pi Pico W. Elle est basée sur le système d'interface Grove, qui est un système de connecteur universel permettant de connecter facilement différents capteurs et modules à des microcontrôleurs, elle est fournie avec différentes modules à savoir :

- [LED Socket Kit](https://wiki.seeedstudio.com/Grove-LED_Socket_Kit/)
- [Button](https://wiki.seeedstudio.com/Grove-Button/#docusaurus_skipToContent_fallback)
- [Rotary Angle Sensor](https://wiki.seeedstudio.com/Grove-Rotary_Angle_Sensor/)
- [Passive Buzzer](https://wiki.seeedstudio.com/Grove-Passive-Buzzer/#docusaurus_skipToContent_fallback)
- [16x2 LCD Screen](https://wiki.seeedstudio.com/Grove-16x2_LCD_Series/#docusaurus_skipToContent_fallback)
- [Sound Sensor](https://wiki.seeedstudio.com/Grove-Sound_Sensor/#docusaurus_skipToContent_fallback)
- [Light Sensor](https://wiki.seeedstudio.com/Grove-Light_Sensor/#docusaurus_skipToContent_fallback)
- [Mini Pir Motion Sensor](https://www.seeedstudio.com/Grove-mini-PIR-motion-sensor-p-2930.html)
- [RGB LED](https://www.ratoeducation.be/fr/grove-rgb-led-ws2813-mini.html)
- [Relay](https://wiki.seeedstudio.com/Grove-Relay/)
- [Temperature&Humidity Sensor](https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/)
- [Mini Fan](https://wiki.seeedstudio.com/Grove-Mini_Fan/#docusaurus_skipToContent_fallback)
- [Analog Servo](https://wiki.seeedstudio.com/Grove-Servo/#docusaurus_skipToContent_fallback)

La carte Grove simplifie les connexions à ces différents modules, ce qui permet aux débutants de pouvoir faire leurs premiers pas dans l'électronique.
La carte Grove est également livrée avec plusieurs bibliothèques pour certains de ses modules qui sont donc déjà préconfigurés et donc beaucoup plus simple à utiliser.
