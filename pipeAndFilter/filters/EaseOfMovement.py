from pipeAndFilter.filters.Filtre import Filtre


class EaseOfMovement(Filtre):
    """Procédure d'exécution du filtre
    @:param action l'action sur laquelle on applique le filtre"""

    def process(self, action):
        data = action.getGraphData()
        emv = list()
        emv14 = list()
        sum = 0
        haut = 0
        bas = 0
        volume = 0

        # Calcul de l'EMV
        for i in range(1, len(data), 1):
            if (data[i]['date'] - data[i - 1]['date']).days == 1:
                emv.append(((((data[i]['data'][1] + data[i]['data'][2]) / 2) - (
                        (data[i - 1]['data'][1] - data[i - 1]['data'][2]) / 2)) / (
                                    data[i]['data'][4] / (data[i]['data'][1] - data[i]['data'][2]))) * 10000)
            elif (data[i]['date'] - data[i - 1]['date']).days == 3:
                haut = (data[i]['data'][1] + data[i - 1]['data'][1]) / 3
                bas = (data[i]['data'][2] + data[i - 1]['data'][2]) / 3
                volume = (data[i]['data'][4] + data[i - 1]['data'][4]) / 3

                # samedi
                emv.append(((((haut + bas) / 2) - ((data[i - 1]['data'][1] - data[i - 1]['data'][2]) / 2)) / (
                            volume / (haut - bas))) * 10000)
                # dimanche
                emv.append(((((haut + bas) / 2) - ((haut - bas) / 2)) / (volume / (haut - bas))) * 10000)
                # lundi
                emv.append(((((data[i]['data'][1] + data[i]['data'][2]) / 2) - ((haut - bas) / 2)) / (
                            data[i]['data'][4] / (data[i]['data'][1] - data[i]['data'][2]))) * 10000)

        # Calcul de l'EMV(14) //moyenne mobile sur 14 jours de l'EMV
        for i in range(13, len(emv), 1):
            for j in range(14):
                sum += emv[i - j]
            emv14.append(sum)
            sum = 0

        # Calcul de la note
        if emv14[len(emv14) - 1] > 0:
            action.addNote(10)
        elif emv14[len(emv14) - 1] < 0:
            action.addNote(-10)
        else:
            action.addNote(0)
