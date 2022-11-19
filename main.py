from view import *

# Architecture MVC : model #
parameters = Parameters(0)

# Architecture MVC : view #
gamescreen = Screen()

# Architecture MVC : controller #
controller = Controller()

# Démarrage de l'application #
gamescreen.runmenu(parameters, gamescreen, controller)
