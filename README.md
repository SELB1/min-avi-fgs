# min-avi-fgs

## Installation

Installation des dépendances (python-ivy, colorama)

```
pip install -r requirements.txt
```

## Intégration

### Intégration dans un autre programme

* Installer le module ``fgs`` (placer le dossier ``fgs`` dans le répertoire contenant le main.py)
* Importer la fonction ``bind_messages`` comme suit : ``from fgs.main import bind_messages`` depuis le main
* ``bind_messages`` contient tous les appels de ``IvyBindMsg(...)``

### Intégration sur le bus Ivy

* Lancer le ``main.py`` se trouvant à la racine du dépot

```
$ python main.py -h
usage: FGS [-h] [-b IVY_ADDRESS] [-p FP_PATH] [-v]

Connects to the Ivy bus and sends the messages according to specs

options:
  -h, --help      show this help message and exit
  -b IVY_ADDRESS  Ivy bind adress (127.255.255.255:2010 by default)
  -p FP_PATH      Path to the CSV flightplan (data/flightplan.csv by default)
  -v              Enable log messages (disabled by default)
```

## Messages IVY envoyés

### Vent et déclinaison magnétique

```
^MagneticDeclination=(\S+)
^WindComponent VWind=(\S+) dirWind=(\S+)
```

* Déclinaison magnétique et angle du vent en radians.
* Vitesse du vent en m/s.

### Limites facteurs de charge

```
^LimitsN nx_neg=(\S+) nx_pos=(\S+) nz_neg=(\S+) nz_pos=(\S+)
^LimitsNAP nx_neg_AP=(\S+) nx_pos_AP=(\S+) nz_neg_AP=(\S+) nz_pos_AP=(\S+)
```

nz_pos : limite supérieure de nz

nz_neg : limite inférieure de nz

Unités m/s².

### Vitesse managée et limites de vitesse

```
^SpeedLimits vmin=(\S+) vmax=(\S+)
^ManagedSpeed vi=(\S+) 
```

Unités : m/s

### Angle et vitesse d'angle de roulis manuel et AP

```
^RollLimits phimax=(\S+) pmax=(\S+)
^RollLimitsAP phimax_AP=(\S+) pmax_AP=(\S+)
```

Unités : degrés et °/s

### Axe à capturer

```
^Axis x=(\S+) y=(\S+) chi=(\S+)
```

* (x,z) : origine de l'axe (m)
* chi : angle de l'axe, par rapport au nord vrai (en °, entre 0 et 359)

### Altitude managée

```
^ManagedAlt alt=(\S+) Q=(\S+)
```

* alt : altitude pression (en ft)
* Q : réference de pression (en hPa)

## Messages IVY écoutés

### DIRTO

```
^DIRTO x=(\S+) y=(\S+)
```

x, y en m

x croissant vers le Nord, y croissant vers l'Est