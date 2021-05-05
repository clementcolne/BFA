from Filtre import Filtre
import copy
from operator import attrgetter
from operator import itemgetter


class Resistance(Filtre):
    """Procédure d'exécution du filtre
    @:param action l'action sur laquelle on applique le filtre"""

    def process(self, action):
        # Le filtre commence par récupérer les données graphiques de l'action
        data = action.getGraphData()
        clotureData = list()

        # On filtre les données pour ne garder que les coûts de clotures qui servent à tracer la courbe
        for row in data:
            clotureData.append({'date': row['date'], 'cout': row['data'][3]})

        # Récupération des points les plus hauts de la courbe
        copie = copy.deepcopy(clotureData)
        maxs = list()

        for i in range(5):
            maxs.append(max(copie, key=itemgetter('cout')))
            copie.remove(maxs[len(maxs) - 1])
        sorted(maxs, key=itemgetter('date'))

        # Calcul de la pente
        p = 0
        for i in range(len(maxs) - 1):
            for j in range(i + 1, len(maxs) - 1, 1):
                p += (maxs[j]['cout'] - maxs[i]['cout']) / int((maxs[j]['date'] - maxs[i]['date']).days)
        p = p / len(maxs)

        # Ajout d'une donne à l'action
        if p > 0:
            action.addNote(10)
        elif p < 0:
            action.addNote(-10)
        else:
            action.addNote(0)