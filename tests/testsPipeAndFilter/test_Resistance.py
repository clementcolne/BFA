from unittest import TestCase
from pipeAndFilter.filters.Resistance import Resistance
from models.Action import Action
from tools.ConfigTest import ConfigTest


class TestResistance(TestCase):
    def test_process_hausse(self):
        # Création des objets pour les tests
        actionTest1 = Action("Test1")
        actionTest2 = Action("Test2")
        actionTest3 = Action("Test3")
        res = Resistance()

        # Test 1
        actionTest1.remplirGraph(ConfigTest.get_graph_hausse())

        # Exécution du test
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), 10)

        # Test 2
        actionTest2.remplirGraph(ConfigTest.get_graph_hausse())
        res.process(actionTest2)
        actionTest2.calculFinalNote()

        self.assertEqual(actionTest2.getFinalNote(), 10)

        # Test 3
        actionTest3.remplirGraph(ConfigTest.get_graph_hausse())
        res.process(actionTest3)
        actionTest3.calculFinalNote()

        self.assertEqual(actionTest3.getFinalNote(), 10)

    def test_process_baisse(self):
        actionTest1 = Action("Test1")
        actionTest2 = Action("Test2")
        actionTest3 = Action("Test3")
        res = Resistance()

        # Test 1
        actionTest1.remplirGraph(ConfigTest.get_graph_baisse())
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), -10)

        # Test 2
        actionTest2.remplirGraph(ConfigTest.get_graph_baisse())
        res.process(actionTest2)
        actionTest2.calculFinalNote()

        self.assertEqual(actionTest2.getFinalNote(), -10)

        # Test 3
        actionTest3.remplirGraph(ConfigTest.get_graph_baisse())
        res.process(actionTest3)
        actionTest3.calculFinalNote()

        self.assertEqual(actionTest3.getFinalNote(), -10)

    def test_process_stable(self):
        actionTest1 = Action("Test1")
        res = Resistance()

        actionTest1.remplirGraph(ConfigTest.get_graph_stable())
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), 0)
