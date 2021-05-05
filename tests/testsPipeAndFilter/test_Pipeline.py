from unittest import TestCase
from datetime import date
from models.Action import Action
from pipeAndFilter.Pipeline import Pipeline
from pipeAndFilter.filters.Resistance import Resistance
from pipeAndFilter.filters.Support import Support


class TestPipeline(TestCase):
    """Procédure de test de l'ajout de fonctions filtres dans le pipeline"""
    def test_add_filter(self):
        # Création des pipelines de tests
        pipe1 = Pipeline()
        pipe2 = Pipeline()
        pipe3 = Pipeline()
        pipe4 = Pipeline()

        # Créations des filtres à ajouter aux pipelines
        def filtre1():
            return

        def filtre2():
            return

        def filtre3():
            return

        def filtre4():
            return

        def filtre5():
            return

        # Tests 1
        pipe1.addFilter([filtre1, filtre2, filtre3])

        self.assertTrue(pipe1.filterLen() == 3)

        # Tests 2
        pipe2.addFilter([filtre1])

        self.assertTrue(pipe2.filterLen() == 1)

        # Tests 3
        pipe3.addFilter([filtre1, filtre2, filtre3, filtre4, filtre5])

        self.assertTrue(pipe3.filterLen() == 5)

        # Tests 4
        pipe4.addFilter([filtre1, filtre3])

        self.assertTrue(pipe4.filterLen() == 2)

    """Procédure de test de l'exécution du pipeline"""
    def test_execute(self):
        # Création des variables de tests
        actionTest = Action("Orange")
        pipe = Pipeline()

        # Création des fonctions filtres
        def filtre1(action):
            action.addNote(1)

        def filtre2(action):
            action.addNote(2)

        def filtre3(action):
            action.addNote(3)

        # Ajout des filtres dans le pipe
        pipe.addFilter([filtre1, filtre2, filtre3])

        # Exécution du pipe
        pipe.execute(actionTest)
        actionTest.calculFinalNote()

        self.assertTrue(actionTest.getFinalNote() == 6)

        # Ajout de filtres supplémentaires pour tests
        def filtre4(action):
            action.addNote(4)

        def filtre5(action):
            action.addNote(5)

        pipe.addFilter([filtre4, filtre5])
        pipe.execute(actionTest)
        actionTest.calculFinalNote()

        self.assertEqual(actionTest.getFinalNote(), 27)

        #Encore des filtres pour tester
        def filtre6(action):
            action.addNote(6)

        def filtre7(action):
            action.addNote(7)

        pipe.addFilter([filtre6, filtre7])
        pipe.execute(actionTest)
        actionTest.calculFinalNote()

        self.assertEqual(actionTest.getFinalNote(), 76)

    def test_with_class_filters(self):
        # Création des objets pour les tests
        actionTest1 = Action("Test1")
        actionTest2 = Action("Test2")
        actionTest3 = Action("Test3")
        graphData1 = list()
        graphData2 = list()
        graphData3 = list()
        pipe = Pipeline()
        res = Resistance()
        sup = Support()

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
        pipe.addFilter([res, sup])
        pipe.execute(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), 20)

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
        pipe.execute(actionTest2)
        actionTest2.calculFinalNote()

        self.assertEqual(actionTest2.getFinalNote(), -20)

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

        actionTest3.remplirGraph(graphData3)
        pipe.execute(actionTest3)
        actionTest3.calculFinalNote()

        self.assertEqual(actionTest3.getFinalNote(), 0)
