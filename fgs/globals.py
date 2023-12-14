"""
Variables globales du module, partagées par les fonctions et mises à jour par les callback Ivy
"""

# NOTE IMPORTANTE: Veiller à utiliser la bonne instruction pour importer les variables globales !

# Bonne manière de faire : accède à la dernière valeur de la variable s'il elle a été modifiée
# >>> import fgs.globals as fg
# >>> fg.STATE_VECTOR

# Mauvaise manière : ne fonctionne pas et créé une copie de la variable dans le module courant
# >>> from fgs.globals import STATE_VECTOR

STATE_VECTOR = None
TARGETED_LAT_WPT = 1
TARGETED_HGT_WPT = 0
LOG = True
LDG = 0
FLAP = 0
FP_PATH = "data/flightplan.csv"