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
        note = 0
        distance = 0
        box = 0

        # Calcul de l'EMV
        try:
            for i in range(1, len(data), 1):
                distance = (((data[i]['data'][1] + data[i]['data'][2]) / 2) - (
                            (data[i - 1]['data'][1] + data[i - 1]['data'][2]) / 2))
                box = data[i]['data'][4] / (data[i]['data'][1] - data[i]['data'][2])
                emv.append((distance/box)*10000)
        except ZeroDivisionError:
            action.addNote(0)
            return

        # Calcul de l'EMV(14) //moyenne mobile sur 14 jours de l'EMV
        for i in range(13, len(emv), 1):
            for j in range(14):
                sum += emv[i - j]
            emv14.append(sum/14)
            sum = 0

        # Calcul de la note
        if emv14[len(emv14) - 1] > 0:
            note += 10
            for i in range(5):
                if emv14[len(emv14) - 1 - i] > emv14[len(emv14) - 2 - i]:
                    note += 1
                elif emv14[len(emv14) - 1 - i] < emv14[len(emv14) - 2 - i]:
                    note -= 1
        elif emv14[len(emv14) - 1] < 0:
            note -= 10
            for i in range(5):
                if emv14[len(emv14) - 1 - i] > emv14[len(emv14) - 2 - i]:
                    note += 1
                elif emv14[len(emv14) - 1 - i] < emv14[len(emv14) - 2 - i]:
                    note -= 1
        else:
            note += 0

        action.addNote(note)
