from datetime import date
from random import randint
from random import randrange


class ConfigTest:
    @staticmethod
    def get_graph_hausse():
        # Initialisation des variables
        graphData = list()
        day = 1
        month = 1
        cost = 60
        high = 61
        low = 59

        # Génération du graph
        for i in range(100):
            data = {'date': date(2020, month, day), 'data': [0, high, low, cost, 0]}
            graphData.append(data)

            if i % 5 == 0:
                day += 2
            if day >= 28 and month == 2:
                day = 1
                month += 1
            elif day >= 30:
                day = 1
                month += 1
            else:
                day += 1

            factor = randint(1, 10)
            cost += factor
            high += factor + randint(0, 3)
            low += factor + randint(-2, 0)

        return graphData

    @staticmethod
    def get_graph_baisse():
        # Initialisation des variables
        graphData = list()
        day = 1
        month = 1
        cost = 60
        high = 61
        low = 59

        # Génération du graph
        for i in range(100):
            data = {'date': date(2020, month, day), 'data': [0, high, low, cost, 0]}
            graphData.append(data)

            if i % 5 == 0:
                day += 2
            if day >= 28 and month == 2:
                day = 1
                month += 1
            elif day >= 30:
                day = 1
                month += 1
            else:
                day += 1

            factor = randint(1, 10)
            cost -= factor
            high -= factor + randint(0, 3)
            low -= factor + randint(-2, 0)

        return graphData

    @staticmethod
    def get_graph_stable():
        # Initialisation des variables
        graphData = list()
        day = 1
        month = 1
        cost = 60
        high = 61
        low = 59

        # Génération du graph
        for i in range(100):
            data = {'date': date(2020, month, day), 'data': [0, high, low, cost, 0]}
            graphData.append(data)

            if i % 5 == 0:
                day += 2
            if day >= 28 and month == 2:
                day = 1
                month += 1
            elif day >= 30:
                day = 1
                month += 1
            else:
                day += 1

            factor = randrange(-5, 0)
            if day % 3 == 0:
                cost -= factor
            else:
                cost += factor
            high += factor + randint(0, 3)
            low += factor + randrange(-2, 0)

        return graphData
