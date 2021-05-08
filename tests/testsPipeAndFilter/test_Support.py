from unittest import TestCase
from pipeAndFilter.filters.Support import Support
from models.Action import Action
from tools.ConfigTest import ConfigTest


class TestSupport(TestCase):
    def test_process_hausse(self):
        # Création des objets pour les tests
        actionTest1 = Action("Test1")
        actionTest2 = Action("Test2")
        actionTest3 = Action("Test3")
        res = Support()

        # Initialisation des données graphiques de tests
        actionTest1.remplirGraph(ConfigTest.get_graph_hausse())

        # Exécution du test
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), 10)

    def test_process_baisse(self):
        actionTest1 = Action("Test1")
        res = Support()

        actionTest1.remplirGraph(ConfigTest.get_graph_baisse())
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), -10)

    def test_process_stable(self):
        actionTest1 = Action("Test1")
        res = Support()

        actionTest1.remplirGraph(ConfigTest.get_graph_stable())
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), 0)
