from pipeAndFilter.Pipeline import Pipeline
from pipeAndFilter.filters.Resistance import Resistance
from pipeAndFilter.filters.Support import Support
from pipeAndFilter.filters.MoyenneArithmetique import MoyenneArithmetique


class Algorithme:
    """Procédure statique qui applique le pipe and filter à une action"""
    @staticmethod
    def Notation(action):
        # Création du pipeline
        pipe = Pipeline()

        # Création des filtres
        res = Resistance()
        sup = Support()
        ma = MoyenneArithmetique()

        # Ajout des filtres au pipeline et exécution
        pipe.addFilter([res, sup, ma])
        pipe.execute(action)

        # Calcul de la note finale de l'action
        action.calculFinalNote()
