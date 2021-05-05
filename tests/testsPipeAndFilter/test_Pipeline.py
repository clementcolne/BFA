from unittest import TestCase
from models.Action import Action
from pipeAndFilter.Pipeline import Pipeline
from pipeAndFilter.filters.Resistance import Resistance
from pipeAndFilter.filters.Support import Support
from tools.ConfigTest import ConfigTest


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

        # Encore des filtres pour tester
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
        pipe = Pipeline()
        res = Resistance()
        sup = Support()

        actionTest1.remplirGraph(ConfigTest.get_graph_hausse())

        # Exécution du test
        pipe.addFilter([res, sup])
        pipe.execute(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), 20)

        # Test 2
        actionTest2.remplirGraph(ConfigTest.get_graph_baisse())
        pipe.execute(actionTest2)
        actionTest2.calculFinalNote()

        self.assertEqual(actionTest2.getFinalNote(), -20)

        # Test 3
        actionTest3.remplirGraph(ConfigTest.get_graph_stable())
        pipe.execute(actionTest3)
        actionTest3.calculFinalNote()

        self.assertEqual(actionTest3.getFinalNote(), 0)
