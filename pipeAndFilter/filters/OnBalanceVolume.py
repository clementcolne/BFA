from pipeAndFilter.filters.Filtre import Filtre


class OnBalanceVolume(Filtre):

    """
    @param self: objet de la classe
    @param action: Action sur laquelle on applique le filtre
    """
    def process(self, action):
        data = action.getGraphData()
        obv = list()
        cost = list()
        tmp = list()
        p1 = 0
        p2 = 0

        # On garde les données qui nous intéressent pour le calcul de l'OBV
        for row in data:
            cost.append({'date': row['date'], 'cout': row['data'][3], 'volume': row['data'][4]})

        # Calcul de l'OBV
        obv.append(cost[0]['volume'])

        try:
            for i in range(1, len(cost), 1):
                obv.append(obv[len(obv) - 1] + (
                        (cost[i]['cout'] - cost[i - 1]['cout']) / abs(cost[i]['cout'] - cost[i - 1]['cout'])) * cost[i][
                               'volume'])
        except ZeroDivisionError:
            action.addNote(0)
            return

        # Calcul hausse ou baisse de l'OBV sur les derniers jours
        for i in range(20, 1, -1):
            tmp.append(obv[len(obv) - i])

        for i in range(len(tmp) - 1):
            for j in range(i + 1, len(tmp), 1):
                p1 += (tmp[j] - tmp[i]) / int((cost[len(cost) - 20 + j]['date'] - cost[len(cost) - 20 + i]['date']).days)
        p1 = p1 / len(tmp)

        # Calcul hausse ou baisse des couts sur les derniers jours
        tmp.clear()
        for i in range(20, 0, -1):
            tmp.append(cost[len(cost) - i]['cout'])

        for i in range(len(tmp) - 1):
            for j in range(i + 1, len(tmp), 1):
                if cost[len(cost) - 20 + j]['date'] != cost[len(cost) - 20 + i]['date']:
                    p2 += (tmp[j] - tmp[i]) / int((cost[len(cost) - 20 + j]['date'] - cost[len(cost) - 20 + i]['date']).days)
        p2 = p2 / len(tmp)

        # Résultat des tests
        if p1 > 0 and p2 > 0:
            action.addNote(20)
        elif p1 > 0 and p2 < 0:
            action.addNote(10)
        elif p1 < 0 and p2 < 0:
            action.addNote(-20)
        elif p1 < 0 and p2 > 0:
            action.addNote(-10)
        else:
            action.addNote(0)
