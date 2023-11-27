# min-avi-fgs

## Messages IVY

### Vent et déclinaison magnétique
```
^MagneticDeclination=(\S+)
^WindComponent VWind=(\S+) dirWind=(\S+)
```

Déclinaison magnétique et angle du vent en degrés.
Vitesse du vent en m/s.

### Limites facteurs de charge
```
^LimitsN nx=(\S+) nz=(\S+) nx_AP=(\S+) nz_AP=(\S+)
```
Unités m/s².

### Vitesse managée et limites de vitesse
```
^SpeedLimits vmin=(\S+) vmax=(\S+)
^ManagedSpeed vi=(\S+) 
```
Unités : m/s

### Angle et vitesse d'angle de roulis
```
^RollLimits phimax=(\S+) pmax=(\S+)
```
Unités : degrés et °/s

### Axe à capturer
```
^Axis x=(\S+) z=(\S+) chi=(\S+)
```

* (x,z) : origine de l'axe (m)
* chi : angle de l'axe, par rapport au nord vrai (°)

### Altitude managée
```
^ManagedAlt alt=(\S+) Q=(\S+)
```
alt : altitude pression (en ft)
Q : réference de pression (en hPa)