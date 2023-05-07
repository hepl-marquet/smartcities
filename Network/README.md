![Introduction](https://user-images.githubusercontent.com/124889426/236695960-85dd543e-c005-4421-bf3b-e7c21b3b01fe.png)

Dans cette dernière partie nous allons voir comment connecter notre RPi Pico W au réseau WiFi, pour cela nous allons utiliser la librairie network et sa classe WLAN ainsi qu'un dictionnaire "[secrets.py](secrets.py)".

## La librairie network

### Quelques commandes utiles

Dans les programmes qui vont suivre nous utiliserons :

```network.WLAN(interface_id)``` : Crée un objet d'interface réseau.

```WLAN.active([is_active])``` : Active l'interface réseau.

```WLAN.connect(ssid=None, key=None, *, bssid=None)``` : Crée la connexion au réseau ssid correspond au nom du réseau et key correspond au mot de passe.

```WLAN.disconnect()``` : Rompt la connexion au réseau.

![LesDiffCodes](https://user-images.githubusercontent.com/124889426/236696105-263a380f-ed36-4ea1-a73d-e6873bfc2d7f.png)

## [NETWORK_BASICS](NETWORK_BASICS.py)
- Programme qui établit une connexion avec un réseau WiFi.

```
#Importation des librairies
import network           #Librairie pour se connecter au WiFi
from utime               #Librairie pour le temps
from secrets import *    #Dictionnaire contenant les informations de connexion au WiFi

wlan = network.WLAN(network.STA_IF)                       #Création et initialisation de l'objet WLAN.
wlan.active(True)                                         #Activation de l'interface réseau
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"])  #Connexion au réseau WiFi avec les identifiants précisés dans le dictionnaire secrets

#Affichage d'un message dans la console pour signaler que le code est en cours d'éxécution.
print("Connection to WiFi network.")
print("---------------------------")
print("Trying to connect to WiFi...")
print()

#Boucle pour se connecter
retry = 10                                                #Nombre de tentatives
while (retry > 0):
    wlan_stat=wlan.status()                               #Statut de la connexion et renvoi des erreurs en cas de problème.
    if wlan_stat==3:
        print("Got IP")
        break
    if wlan_stat==-1:
        raise RuntimeError('WiFi connection failed')
    if wlan_stat==-2:
        raise RuntimeError('No AP found')    
    if wlan_stat==-3:
        raise RuntimeError('Wrong WiFi password')
    
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    retry = retry-1
    utime.sleep(1)

if wlan_stat!=3:
    raise RuntimeError('WiFi connection failed')

#Affichage du nom du WiFi et des informations du client.
print()
print('Connected to WiFi network: ',end="")
print(wlan.config("ssid"))
print()
ip=wlan.ifconfig()
print("IP info (IP address, mask, gateway, DNS):")
print(ip)
print()

#On rompt la connexion.
wlan.disconnect()
```
