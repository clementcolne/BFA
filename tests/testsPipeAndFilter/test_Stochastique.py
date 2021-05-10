from unittest import TestCase
from models.Action import Action
from pipeAndFilter.filters.Stochastique import Stochastique
from tools.ConfigTest import ConfigTest


class TestStochastique(TestCase):
    def test_process_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        sto = Stochastique()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_hausse())
        sto.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() == 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_hausse())
        sto.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action2.getFinalNote() == 0)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_hausse())
        sto.process(action3)
        action3.calculFinalNote()

        self.assertEqual(action3.getFinalNote(), 0)

    def test_process_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        sto = Stochastique()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_baisse())
        sto.process(action1)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), -10)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_baisse())
        sto.process(action2)
        action2.calculFinalNote()

        self.assertEqual(action2.getFinalNote(), -10)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_baisse())
        sto.process(action3)
        action3.calculFinalNote()

        self.assertEqual(action3.getFinalNote(), -10)

    def test_process_stable(self):
        action1 = Action("Test1")
        sto = Stochastique()

        action1.remplirGraph(ConfigTest.get_graph_stable())
        sto.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() == 0)

    def test_process_change_for_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        sto = Stochastique()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_hausse())
        sto.process(action1)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_hausse())
        sto.process(action2)
        action2.calculFinalNote()

        self.assertEqual(action2.getFinalNote(), 0)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_hausse())
        sto.process(action3)
        action3.calculFinalNote()

        self.assertEqual(action3.getFinalNote(), 0)

    # Note : ajouter une config de test avec un graph plus mouvementé pour tester le Stochastique
