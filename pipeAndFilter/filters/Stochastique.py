from pipeAndFilter.filters.Filtre import Filtre
from operator import itemgetter


class Stochastique(Filtre):
    """Procédure d'exécution du filtre
    @:param action l'action sur laquelle on applique le filtre"""

    def process(self, action):
        data = action.getGraphData()
        cost = list()
        K = list()
        d = list()
        temp = list()
        temp2 = list()
        haut = dict()
        bas = dict()
        p = 0
        note = 0

        # On filtre les données qui servent à tracer la courbe et le stochastique
        for row in data:
            cost.append({'date': row['date'], 'haut': row['data'][1], 'bas': row['data'][2], 'cloture': row['data'][3]})

        # Calcul du stochastique
        for i in range(13, len(cost), 1):
            for j in range(i - 13, i, 1):
                temp.append(cost[j])
            haut = max(temp, key=itemgetter('haut'))
            bas = min(temp, key=itemgetter('bas'))
            if (haut['haut'] - bas['bas']) == 0:
                action.addNote(0)
                return
            K.append(100 * ((cost[i]['cloture'] - bas['bas']) / (haut['haut'] - bas['bas'])))
            d.append(cost[i]['date'])
            temp.clear()

        # On regarde si K est en hausse ou en baisse sur les derniers jours
        for i in range(1, 20, 1):
            temp.append(K[len(K) - i])
            temp2.append(d[len(d) - i])

        # On calcule la pente de K sur les derniers jours
        for i in range(len(temp) - 1):
            for j in range(i + 1, len(temp), 1):
                p += (temp[j] - temp[i]) / int((temp2[j] - temp2[i]).days)
        p = p / len(temp)

        # On regarde si le stochastique est < 20% ou > 80%
        if K[len(K) - 1] > 80 and p < 0:
            note -= 10
        elif K[len(K) - 1] < 20 and p > 0:
            note += 10
        elif K[len(K) - 1] < 20 and p < 0:
            note -= 10
        else:
            note += 0

        action.addNote(note)
