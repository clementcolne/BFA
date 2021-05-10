from pipeAndFilter.filters.Filtre import Filtre


class MoyenneArithmetique(Filtre):
    """Procédure d'exécution du filtre
    @:param action l'action sur laquelle on applique le filtre"""

    def process(self, action):
        # Initialisation des variables
        data = action.getGraphData()
        mma20 = list()
        mma50 = list()
        cost = list()
        sum = 0
        note = 0

        # On filtre les données pour ne garder que les coûts de clotures qui servent à tracer la courbe
        for row in data:
            cost.append({'date': row['date'], 'cout': row['data'][3]})

        # Calcul de la MMA20    //Calcul sur 20 séances, à ajuster par la suite à 20 jours
        for i in range(20, len(cost), 1):
            for j in range(20):
                sum += cost[i - j]['cout']
            mma20.append(sum / 20)

        # Calcul de la MMA50    //Idem que MMA20
        sum = 0
        for i in range(50, len(cost), 1):
            for j in range(50):
                sum += cost[i - j]['cout']
            mma50.append(sum / 50)

        # Test si la MMA20 > MMA50
        if mma20[len(mma20) - 1] > mma50[len(mma50) - 1]:
            note += 20
        elif mma20[len(mma20) - 1] < mma50[len(mma50) - 1]:
            note -= 20
        else:
            note += 0

        # Test MMA20 en hausse ou en baisse
        for i in range(20):
            # MMA20 en hausse -> on augmente la note
            if mma20[len(mma20) - 1 - i] > mma20[len(mma20) - 2 - i]:
                note += 1
            # MMA20 en baisse -> on diminue la note
            elif mma20[len(mma20) - 1 - i] < mma20[len(mma20) - 2 - i]:
                note -= 1
            else:
                note += 0

        action.addNote(note)
