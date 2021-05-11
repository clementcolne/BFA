from pipeAndFilter.filters.Filtre import Filtre


class MoyenneExponentielle(Filtre):
    """Procédure d'exécution du filtre
    @:param action l'action sur laquelle on applique le filtre"""
    def process(self, action):
        # Initialisation des variables
        data = action.getGraphData()
        mme12 = list()
        mme26 = list()
        macd = list()
        mme9 = list()
        cost = list()
        sum = 0
        diff = 0
        note = 0

        # On filtre les données pour ne garder que les coûts de clotures qui servent à tracer la courbe
        for row in data:
            cost.append({'date': row['date'], 'cout': row['data'][3]})

        # Calcul de la MME12
        for i in range(12):
            sum += cost[i]['cout']
        mme12.append(sum / 12 + (2 / 13) * (cost[12]['cout'] - sum / 12))

        for i in range(13, len(cost), 1):
            mme12.append(mme12[len(mme12) - 1] + (2 / 13) * (cost[i]['cout'] - mme12[len(mme12) - 1]))

        # Calcul de la MME26
        sum = 0
        for i in range(26):
            sum += cost[i]['cout']
        mme26.append(sum / 26 + (2 / 27) * (cost[26]['cout'] - sum / 26))

        for i in range(27, len(cost), 1):
            mme26.append(mme26[len(mme26) - 1] + (2 / 27) * (cost[i]['cout'] - mme26[len(mme26) - 1]))

        # Calcul de la MACD
        diff = len(mme12) - len(mme26)
        for i in range(len(mme26)):
            macd.append(mme12[i + diff] - mme26[i])

        # Calcul de la MME9 à partir de la courbe MACD  //Courbe signal de la MACD
        sum = 0
        for i in range(9):
            sum += macd[i]
        mme9.append(sum / 9 + (2 / 10) * (macd[9] - sum / 9))

        for i in range(10, len(macd), 1):
            mme9.append(mme9[len(mme9) - 1] + (2 / 10) * (macd[i] - mme9[len(mme9) - 1]))

        # Test si la MACD > MME9
        if macd[len(macd) - 1] > mme9[len(mme9) - 1]:
            note += 20
        elif macd[len(macd) - 1] < mme9[len(mme9) - 1]:
            note -= 20
        else:
            note += 0

        # Test MACD en hausse ou en baisse
        for i in range(14):
            # MACD en hausse -> on augmente la note
            if macd[len(macd) - 1 - i] > macd[len(macd) - 2 - i]:
                note += 1
            # MACD en baisse -> on diminue la note
            elif macd[len(macd) - 1 - i] < macd[len(macd) - 2 - i]:
                note -= 1
            else:
                note += 0

        action.addNote(note)
