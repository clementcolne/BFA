from unittest import TestCase
from ConfigTest import ConfigTest
from pipeAndFilter.filters.MouvementDirectionnel import MouvementDirectionnel
from models.Action import Action


class TestMouvementDirectionnel(TestCase):
    def test_process_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        mv = MouvementDirectionnel()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_hausse())
        mv.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() > 20)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_hausse())
        mv.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action2.getFinalNote() > 20)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_hausse())
        mv.process(action3)
        action3.calculFinalNote()

        self.assertTrue(action3.getFinalNote() > 20)

    def test_process_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        mv = MouvementDirectionnel()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_baisse())
        mv.process(action1)
        action1.calculFinalNote()

        self.assertTrue(-20 < action1.getFinalNote() <= -10)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_baisse())
        mv.process(action2)
        action2.calculFinalNote()

        self.assertTrue(-20 < action2.getFinalNote() <= -10)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_baisse())
        mv.process(action3)
        action3.calculFinalNote()

        self.assertTrue(-20 < action3.getFinalNote() <= -10)

    def test_process_change_for_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        mv = MouvementDirectionnel()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_hausse())
        mv.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() < -10)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_hausse())
        mv.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action2.getFinalNote() < -10)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_hausse())
        mv.process(action3)
        action3.calculFinalNote()

        self.assertTrue(action3.getFinalNote() < -10)
