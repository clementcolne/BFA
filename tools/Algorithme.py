from pipeAndFilter.Pipeline import Pipeline
from pipeAndFilter.filters.Resistance import Resistance
from pipeAndFilter.filters.Support import Support
from pipeAndFilter.filters.MoyenneArithmetique import MoyenneArithmetique
from pipeAndFilter.filters.MoyenneExponentielle import MoyenneExponentielle
from pipeAndFilter.filters.OnBalanceVolume import OnBalanceVolume
from pipeAndFilter.filters.Stochastique import Stochastique
from pipeAndFilter.filters.MouvementDirectionnel import MouvementDirectionnel
from pipeAndFilter.filters.EaseOfMovement import EaseOfMovement


class Algorithme:

    """
    @param action: Action à noter
    """
    @staticmethod
    def Notation(action):
        if len(action.getGraphData()) == 0:
            return

        # Création du pipeline
        pipe = Pipeline()

        # Création des filtres
        res = Resistance()
        sup = Support()
        ma = MoyenneArithmetique()
        me = MoyenneExponentielle()
        obv = OnBalanceVolume()
        sto = Stochastique()
        md = MouvementDirectionnel()
        eom = EaseOfMovement()

        # Ajout des filtres au pipeline et exécution
        pipe.addFilter([res, sup, ma, me, obv, sto, md, eom])
        pipe.execute(action)

        # Calcul de la note finale de l'action
        action.calculFinalNote()
