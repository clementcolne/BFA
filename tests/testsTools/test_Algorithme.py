from unittest import TestCase
from tools.Algorithme import Algorithme
from tools.ConfigTest import ConfigTest
from models.Action import Action


class TestAlgorithme(TestCase):
    def test_notation(self):
        # Création des objets pour les tests
        actionTest1 = Action("Test1")
        actionTest2 = Action("Test2")
        actionTest3 = Action("Test3")

        actionTest1.remplirGraph(ConfigTest.get_graph_hausse())

        # Exécution du test
        Algorithme.Notation(actionTest1)

        self.assertTrue(actionTest1.getFinalNote() >= 60)

        # Test 2
        actionTest2.remplirGraph(ConfigTest.get_graph_baisse())
        Algorithme.Notation(actionTest2)

        self.assertTrue(actionTest2.getFinalNote() <= -60)

        # Test 3
        actionTest3.remplirGraph(ConfigTest.get_graph_stable())
        Algorithme.Notation(actionTest3)

        self.assertTrue(60 > actionTest3.getFinalNote() > -60)
