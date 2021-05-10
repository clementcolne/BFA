from pipeAndFilter.filters.Filtre import Filtre
from math import floor


class MouvementDirectionnel(Filtre):
    """Procédure d'exécution du filtre
    @:param action l'action sur laquelle on applique le filtre"""

    def process(self, action):
        data = action.getGraphData()
        tr = list()
        tr14 = list()
        dmp = list()  # DM+
        dmm = list()  # DM-
        dm14p = list()
        dm14m = list()
        dip = list()  # DI+
        dim = list()  # DI-
        adx = list()
        sump = 0
        summ = 0
        sum = 0
        note = 0

        # Calcul des DM+ et DM-
        for i in range(len(data) - 1):
            dmp.append(max(data[1 + i]['data'][1] - data[i]['data'][1], 0))
            dmm.append(max(data[i]['data'][2] - data[1 + i]['data'][2], 0))

        for i in range(14):
            sump += dmp[i]
            summ += dmm[i]
        dm14p.append(sump)
        dm14m.append(summ)

        # Calcul des suites DMn+ et DMn-
        for i in range(14, len(dmp), 1):
            dm14p.append((13 / 14) * dm14p[14 - i] + dmp[i])
            dm14m.append((13 / 14) * dm14m[14 - i] + dmm[i])

        # Calcul des TR
        for i in range(1, len(data), 1):
            tr.append(
                max(abs(data[i]['data'][1] - data[i]['data'][2]), abs(data[i]['data'][2] - data[i - 1]['data'][3]),
                    abs(data[i]['data'][2] - data[i - 1]['data'][3])))

        # Calcul de la suite TRn
        for i in range(14):
            sum += tr[i]
        tr14.append(sum)

        for i in range(14, len(tr), 1):
            tr14.append((13 / 14) * tr14[14 - i] + tr[i])

        # Calcul des DI+ et DI-
        for i in range(len(tr14)):
            dip.append((dm14p[i] / tr14[i]) * 100)
            dim.append((dm14m[i] / tr14[i]) * 100)

        # Calcul de l'ADX
        sum = 0
        for i in range(14, 27, 1):
            sum += floor((abs(dip[i] - dim[i]) / (dip[i] + dim[i])) * 100)
        adx.append((1 / 14) * sum)

        for i in range(15, len(dip), 1):
            adx.append((13 * adx[i - 15] + floor((abs(dip[i] - dim[i]) / (dip[i] + dim[i])) * 100)) / 14)

        # Calcul de la note à donner à l'action
        if adx[len(adx) - 1] < 25:
            action.addNote(0)
            return

        if dip[len(dip) - 1] > dim[len(dim) - 1]:
            note += 20
            for i in range(10):
                if adx[len(adx) - 1 - i] > adx[len(adx) - 2 - i]:
                    note += 1
                elif adx[len(adx) - 1 - i] < adx[len(adx) - 2 - i]:
                    note -= 1
                else:
                    note += 0
        elif dip[len(dip) - 1] < dim[len(dim) - 1]:
            note -= 20
            for i in range(10):
                if adx[len(adx) - 1 - i] > adx[len(adx) - 2 - i]:
                    note += 1
                elif adx[len(adx) - 1 - i] < adx[len(adx) - 2 - i]:
                    note -= 1
                else:
                    note += 0

        action.addNote(note)
