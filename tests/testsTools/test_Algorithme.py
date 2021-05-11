from unittest import TestCase
from tools.Algorithme import Algorithme
from tools.ConfigTest import ConfigTest
from models.Action import Action


class TestAlgorithme(TestCase):
    def test_notation_hausse(self):
        # Création des objets pour les tests
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_hausse())
        Algorithme.Notation(action1)

        self.assertTrue(action1.getFinalNote() > 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_hausse())
        Algorithme.Notation(action2)

        self.assertTrue(action2.getFinalNote() > 0)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_hausse())
        Algorithme.Notation(action3)

        self.assertTrue(action3.getFinalNote() > 0)

    def test_notation_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_baisse())
        Algorithme.Notation(action1)

        self.assertTrue(action1.getFinalNote() < 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_baisse())
        Algorithme.Notation(action2)

        self.assertTrue(action2.getFinalNote() < 0)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_baisse())
        Algorithme.Notation(action3)

        self.assertTrue(action3.getFinalNote() < 0)

    def test_notation_change_for_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_hausse())
        Algorithme.Notation(action1)

        self.assertTrue(action1.getFinalNote() > 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_hausse())
        Algorithme.Notation(action2)

        self.assertTrue(action2.getFinalNote() > 0)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_hausse())
        Algorithme.Notation(action3)

        self.assertTrue(action3.getFinalNote() > 0)

    def test_notation_change_for_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_baisse())
        Algorithme.Notation(action1)

        self.assertTrue(action1.getFinalNote() < 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_baisse())
        Algorithme.Notation(action2)

        self.assertTrue(action2.getFinalNote() < 0)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_baisse())
        Algorithme.Notation(action3)

        self.assertTrue(action3.getFinalNote() < 0)
