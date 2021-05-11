from unittest import TestCase
from models.Action import Action
from pipeAndFilter.filters.OnBalanceVolume import OnBalanceVolume
from tools.ConfigTest import ConfigTest


class TestOnBalanceVolume(TestCase):
    def test_process_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        obv = OnBalanceVolume()

        action1.remplirGraph(ConfigTest.get_graph_hausse())
        obv.process(action1)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), 10)

        action2.remplirGraph(ConfigTest.get_graph_hausse())
        obv.process(action2)
        action2.calculFinalNote()

        self.assertEqual(action2.getFinalNote(), 10)

        action3.remplirGraph(ConfigTest.get_graph_hausse())
        obv.process(action3)
        action3.calculFinalNote()

        self.assertEqual(action3.getFinalNote(), 10)

    def test_process_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        obv = OnBalanceVolume()

        action1.remplirGraph(ConfigTest.get_graph_baisse())
        obv.process(action1)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), -10)

        action2.remplirGraph(ConfigTest.get_graph_baisse())
        obv.process(action2)
        action2.calculFinalNote()

        self.assertEqual(action2.getFinalNote(), -10)

        action3.remplirGraph(ConfigTest.get_graph_baisse())
        obv.process(action3)
        action3.calculFinalNote()

        self.assertEqual(action3.getFinalNote(), -10)

    def test_process_stable(self):
        action1 = Action("Test1")
        obv = OnBalanceVolume()

        action1.remplirGraph(ConfigTest.get_graph_stable())
        obv.process(action1)
        action1.calculFinalNote()

        # Ne fonctione pas toujours selon les données du graph
        # Beaucoup de faux signaux en période de range
        self.assertEqual(action1.getFinalNote(), 0)

    def test_process_change_for_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        obv = OnBalanceVolume()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_hausse())
        obv.process(action1)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), 10)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_hausse())
        obv.process(action2)
        action2.calculFinalNote()

        self.assertEqual(action2.getFinalNote(), 10)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_hausse())
        obv.process(action3)
        action3.calculFinalNote()

        self.assertEqual(action3.getFinalNote(), 10)

    def test_process_change_for_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        obv = OnBalanceVolume()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_baisse())
        obv.process(action1)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), -10)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_baisse())
        obv.process(action2)
        action2.calculFinalNote()

        self.assertEqual(action2.getFinalNote(), -10)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_baisse())
        obv.process(action3)
        action3.calculFinalNote()

        self.assertEqual(action3.getFinalNote(), -10)
