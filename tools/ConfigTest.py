from datetime import date
from random import randint


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
        for i in range(50):
            data = {'date': date(2020, month, day), 'data': [0, high, low, cost, 0]}
            graphData.append(data)

            if i % 5 == 0:
                day += 3
            if day == 30:
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
        for i in range(50):
            data = {'date': date(2020, month, day), 'data': [0, high, low, cost, 0]}
            graphData.append(data)

            if i % 5 == 0:
                day += 3
            if day == 30:
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
        for i in range(50):
            data = {'date': date(2020, month, day), 'data': [0, high, low, cost, 0]}
            graphData.append(data)

            if i % 5 == 0:
                day += 3
            if day == 30:
                day = 1
                month += 1
            else:
                day += 1
            factor = randint(-10, 10)
            cost += factor
            high += factor + randint(0, 3)
            low += factor + randint(-2, 0)

        return graphData
