# min-avi-fgs

## Installation

Installation des dépendances (python-ivy, colorama)
```
pip install -r requirements.txt
```

## Messages IVY

### Vent et déclinaison magnétique
```
^MagneticDeclination=(\S+)
^WindComponent VWind=(\S+) dirWind=(\S+)
```

* Déclinaison magnétique et angle du vent en degrés.
* Vitesse du vent en m/s.

### Limites facteurs de charge
```
^LimitsN nx=(\S+) nz_pos=(\S+) nz_neg=(\S+) 
^LimitsNAP nx_AP=(\S+) nz_pos_AP=(\S+) nz_neg_AP=(\S+)
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
* chi : angle de l'axe, par rapport au nord vrai (°)

### Altitude managée
```
^ManagedAlt alt=(\S+) Q=(\S+)
```
* alt : altitude pression (en ft)
* Q : réference de pression (en hPa)