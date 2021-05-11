from unittest import TestCase
from tools.ConfigTest import ConfigTest
from models.Action import Action
from pipeAndFilter.filters.EaseOfMovement import EaseOfMovement


class TestEaseOfMovement(TestCase):
    def test_process_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        eom = EaseOfMovement()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_hausse())
        eom.process(action1)
        action1.calculFinalNote()

        self.assertTrue(5 <= action1.getFinalNote() <= 15)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_hausse())
        eom.process(action2)
        action2.calculFinalNote()

        self.assertTrue(5 <= action2.getFinalNote() <= 15)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_hausse())
        eom.process(action3)
        action3.calculFinalNote()

        self.assertTrue(5 <= action3.getFinalNote() <= 15)

    def test_process_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        eom = EaseOfMovement()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_baisse())
        eom.process(action1)
        action1.calculFinalNote()

        self.assertTrue(-15 <= action1.getFinalNote() <= -5)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_baisse())
        eom.process(action2)
        action2.calculFinalNote()

        self.assertTrue(-15 <= action2.getFinalNote() <= -5)

        # Test 3
        action3.remplirGraph(ConfigTest.get_graph_baisse())
        eom.process(action3)
        action3.calculFinalNote()

        self.assertTrue(-15 <= action3.getFinalNote() <= -5)

    def test_process_change_for_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        eom = EaseOfMovement()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_hausse())
        eom.process(action1)
        action1.calculFinalNote()

        self.assertTrue(5 <= action1.getFinalNote() <= 15)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_hausse())
        eom.process(action2)
        action2.calculFinalNote()

        self.assertTrue(5 <= action1.getFinalNote() <= 15)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_hausse())
        eom.process(action3)
        action3.calculFinalNote()

        self.assertTrue(5 <= action1.getFinalNote() <= 15)

    def test_process_change_for_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        eom = EaseOfMovement()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_baisse())
        eom.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() <= -5 or action1.getFinalNote() == 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_baisse())
        eom.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action1.getFinalNote() <= -5 or action1.getFinalNote() == 0)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_baisse())
        eom.process(action3)
        action3.calculFinalNote()

        self.assertTrue(action1.getFinalNote() <= -5 or action1.getFinalNote() == 0)
