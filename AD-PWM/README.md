## AD-PWM

Le RPI Pico dispose d'un ADC permettant de passer d'un signal analogique à un signal digital cependant il ne dispose pas d'un DAC qui permettrait de passer d'un signal digital vers un signal analogique, hors le controle de la luminosité d'une LED se fait via un signal analogique, la librairie PWM nous permet d'envoyer des signaux sous formes d'impulsions qui nous donne la possibilité de simuler des signaux sinusoidaux.

Nous apprendrons donc à utiliser la librairie PWM ainsi que les modules GROVE suivants :

- [Rotary Angle Sensor](https://wiki.seeedstudio.com/Grove-Rotary_Angle_Sensor/)
- [LED Socket Kit](https://wiki.seeedstudio.com/Grove-LED_Socket_Kit/)
- [Passive Buzzer (Bonus)](https://wiki.seeedstudio.com/Grove_passive_Buzzer/)
- [Servo (Bonus)](https://wiki.seeedstudio.com/Grove-Servo/)

## Les différents codes

  - [AD_POTENTIOMETER_BASICS](AD_POTENTIOMETER_BASICS.py)
      - Programme qui permet d'afficher la valeur lue par la pin liée au potentiomètre.
      - On apprend comment configurer une PIN en mode entrée et à lire son entrée.

  - [AD_POTENTIOMETER_LED](AD_POTENTIOMETER_LED.py)
      - Programme qui permet de controller la LED à partir de la valeur du potentiomètre.
      - On lit la donnée du potentiomètre et en fonction de sa valeur avec des conditions if, on peut allumer et éteindre la LED.

  - [PWM_POTENTIOMETER_LED](PWM_POTENTIOMETER_LED.py)
      - Programme qui permet de controller la luminosité d'une LED à l'aide du potentiomètre.
      - On apprend à utiliser les commandes de bases de la librairie PWM.
  - [BONUS_BUZZER_POTENTIOMETER](BONUS_BUZZER_POTENTIOMETER.py)
      - Programme qui permet de controller la fréquence du son que sort le buzzer à l'aide du potentiomètre.
  - [BONUS_SERVO_POTENTIOMETER](BONUS_SERVO_POTENTIOMETER.py)
      - Programme qui permet de controller l'angle du servo moteur à l'aide du potentiomètre.
