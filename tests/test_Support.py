from unittest import TestCase
from datetime import date
from pipeAndFilter.filters.Support import Support
from models.Action import Action


class TestSupport(TestCase):
    def test_process(self):
        # Création des objets pour les tests
        actionTest1 = Action("Test1")
        actionTest2 = Action("Test2")
        actionTest3 = Action("Test3")
        graphData1 = list()
        graphData2 = list()
        graphData3 = list()
        res = Support()

        # Initialisation des données graphiques de tests
        day1 = {'date': date(2020, 1, 1), 'data': [0, 0, 0, 60, 0]}
        day2 = {'date': date(2020, 1, 2), 'data': [0, 0, 0, 70, 0]}
        day3 = {'date': date(2020, 1, 3), 'data': [0, 0, 0, 90, 0]}
        day4 = {'date': date(2020, 1, 4), 'data': [0, 0, 0, 85, 0]}
        day5 = {'date': date(2020, 1, 5), 'data': [0, 0, 0, 87, 0]}
        day6 = {'date': date(2020, 1, 8), 'data': [0, 0, 0, 95, 0]}
        day7 = {'date': date(2020, 1, 9), 'data': [0, 0, 0, 98, 0]}
        day8 = {'date': date(2020, 1, 10), 'data': [0, 0, 0, 93, 0]}
        day9 = {'date': date(2020, 1, 11), 'data': [0, 0, 0, 99, 0]}
        day10 = {'date': date(2020, 1, 12), 'data': [0, 0, 0, 103, 0]}
        day11 = {'date': date(2020, 1, 14), 'data': [0, 0, 0, 101, 0]}
        day12 = {'date': date(2020, 1, 15), 'data': [0, 0, 0, 105, 0]}

        # Ajout des données graphiques dans la liste
        graphData1.append(day1)
        graphData1.append(day2)
        graphData1.append(day3)
        graphData1.append(day4)
        graphData1.append(day5)
        graphData1.append(day6)
        graphData1.append(day7)
        graphData1.append(day8)
        graphData1.append(day9)
        graphData1.append(day10)
        graphData1.append(day11)
        graphData1.append(day12)

        actionTest1.remplirGraph(graphData1)

        # Exécution du test
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), 10)

        # Test 2
        day1 = {'date': date(2020, 1, 1), 'data': [0, 0, 0, 100, 0]}
        day2 = {'date': date(2020, 1, 2), 'data': [0, 0, 0, 96, 0]}
        day3 = {'date': date(2020, 1, 3), 'data': [0, 0, 0, 94, 0]}
        day4 = {'date': date(2020, 1, 4), 'data': [0, 0, 0, 90, 0]}
        day5 = {'date': date(2020, 1, 5), 'data': [0, 0, 0, 91, 0]}
        day6 = {'date': date(2020, 1, 8), 'data': [0, 0, 0, 86, 0]}
        day7 = {'date': date(2020, 1, 9), 'data': [0, 0, 0, 84, 0]}
        day8 = {'date': date(2020, 1, 10), 'data': [0, 0, 0, 88, 0]}
        day9 = {'date': date(2020, 1, 11), 'data': [0, 0, 0, 85, 0]}
        day10 = {'date': date(2020, 1, 12), 'data': [0, 0, 0, 80, 0]}
        day11 = {'date': date(2020, 1, 14), 'data': [0, 0, 0, 77, 0]}
        day12 = {'date': date(2020, 1, 15), 'data': [0, 0, 0, 76, 0]}

        graphData2.append(day1)
        graphData2.append(day2)
        graphData2.append(day3)
        graphData2.append(day4)
        graphData2.append(day5)
        graphData2.append(day6)
        graphData2.append(day7)
        graphData2.append(day8)
        graphData2.append(day9)
        graphData2.append(day10)
        graphData2.append(day11)
        graphData2.append(day12)

        actionTest2.remplirGraph(graphData2)
        res.process(actionTest2)
        actionTest2.calculFinalNote()

        self.assertEqual(actionTest2.getFinalNote(), -10)

        # Test 3
        day1 = {'date': date(2020, 1, 1), 'data': [0, 0, 0, 60, 0]}
        day2 = {'date': date(2020, 1, 2), 'data': [0, 0, 0, 62, 0]}
        day3 = {'date': date(2020, 1, 3), 'data': [0, 0, 0, 59, 0]}
        day4 = {'date': date(2020, 1, 4), 'data': [0, 0, 0, 58, 0]}
        day5 = {'date': date(2020, 1, 5), 'data': [0, 0, 0, 61, 0]}
        day6 = {'date': date(2020, 1, 8), 'data': [0, 0, 0, 60, 0]}
        day7 = {'date': date(2020, 1, 9), 'data': [0, 0, 0, 57, 0]}
        day8 = {'date': date(2020, 1, 10), 'data': [0, 0, 0, 63, 0]}
        day9 = {'date': date(2020, 1, 11), 'data': [0, 0, 0, 61, 0]}
        day10 = {'date': date(2020, 1, 12), 'data': [0, 0, 0, 59, 0]}
        day11 = {'date': date(2020, 1, 14), 'data': [0, 0, 0, 62, 0]}
        day12 = {'date': date(2020, 1, 15), 'data': [0, 0, 0, 60, 0]}

        graphData3.append(day1)
        graphData3.append(day2)
        graphData3.append(day3)
        graphData3.append(day4)
        graphData3.append(day5)
        graphData3.append(day6)
        graphData3.append(day7)
        graphData3.append(day8)
        graphData3.append(day9)
        graphData3.append(day10)
        graphData3.append(day11)
        graphData3.append(day12)

        actionTest3.remplirGraph(graphData2)
        res.process(actionTest2)
        actionTest3.calculFinalNote()

        self.assertEqual(actionTest3.getFinalNote(), 0)
