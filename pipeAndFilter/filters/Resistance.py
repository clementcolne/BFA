from Filtre import Filtre
import copy
from operator import itemgetter


class Resistance(Filtre):

    """
    @param self: objet de la classe
    @param action: Action sur laquelle on applique le filtre
    """
    def process(self, action):
        # Le filtre commence par récupérer les données graphiques de l'action
        data = action.getGraphData()
        clotureData = list()

        # On filtre les données pour ne garder que les coûts de clotures qui servent à tracer la courbe
        for i in range(30, 0, -1):
            clotureData.append({'date': data[len(data) - 1 - i]['date'], 'cout': data[len(data) - 1 - i]['data'][3]})

        # Récupération des points les plus hauts de la courbe
        copie = copy.deepcopy(clotureData)
        maxs = list()

        for i in range(10):
            maxs.append(max(copie, key=itemgetter('cout')))
            copie.remove(maxs[len(maxs) - 1])
        maxs = sorted(maxs, key=itemgetter('date'))

        # Calcul de la pente
        p = 0
        for i in range(len(maxs) - 1):
            for j in range(i + 1, len(maxs), 1):
                p += (maxs[j]['cout'] - maxs[i]['cout']) / int((maxs[j]['date'] - maxs[i]['date']).days)
        p = p / len(maxs)

        # Ajout d'une note à l'action
        if p > 0:
            action.addNote(20)
        elif p < 0:
            action.addNote(-20)
        else:
            action.addNote(0)
