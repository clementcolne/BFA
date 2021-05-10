from unittest import TestCase
from models.Action import Action
from pipeAndFilter.filters.MoyenneArithmetique import MoyenneArithmetique
from tools.ConfigTest import ConfigTest


class TestMoyenneArithmetique(TestCase):
    def test_process_hausse(self):
        # Création des objets pour les tests
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        ma = MoyenneArithmetique()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_hausse())
        ma.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() > 10)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_hausse())
        ma.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action2.getFinalNote() > 10)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_hausse())
        ma.process(action3)
        action3.calculFinalNote()

        self.assertTrue(action3.getFinalNote() > 10)

    def test_process_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        ma = MoyenneArithmetique()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_baisse())
        ma.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() < 10)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_baisse())
        ma.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action2.getFinalNote() < 10)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_baisse())
        ma.process(action3)
        action3.calculFinalNote()

        self.assertTrue(action3.getFinalNote() < 10)

    def test_process_stable(self):
        action1 = Action("Test1")
        ma = MoyenneArithmetique()

        action1.remplirGraph(ConfigTest.get_graph_stable())
        ma.process(action1)
        action1.calculFinalNote()

        # Resultat faux lorsque le graph se construit en hausse ou en baisse
        self.assertTrue(40 > action1.getFinalNote() > -40)

    def test_process_change_for_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        ma = MoyenneArithmetique()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_hausse())
        ma.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() >= 20)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_hausse())
        ma.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action2.getFinalNote() >= 20)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_hausse())
        ma.process(action3)
        action3.calculFinalNote()

        self.assertTrue(action3.getFinalNote() >= 20)
