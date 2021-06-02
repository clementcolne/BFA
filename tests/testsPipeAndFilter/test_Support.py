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

        # Test 1
        actionTest1.remplirGraph(ConfigTest.get_graph_hausse())

        # Exécution du test
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), 20)

        # Test 2
        actionTest2.remplirGraph(ConfigTest.get_graph_hausse())
        res.process(actionTest2)
        actionTest2.calculFinalNote()

        self.assertEqual(actionTest2.getFinalNote(), 20)

        # Test 3
        actionTest3.remplirGraph(ConfigTest.get_graph_hausse())
        res.process(actionTest3)
        actionTest3.calculFinalNote()

        self.assertEqual(actionTest2.getFinalNote(), 20)

    def test_process_baisse(self):
        actionTest1 = Action("Test1")
        actionTest2 = Action("Test2")
        actionTest3 = Action("Test3")
        res = Support()

        # Test 1
        actionTest1.remplirGraph(ConfigTest.get_graph_baisse())
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        self.assertEqual(actionTest1.getFinalNote(), -20)

        # Test 2
        actionTest2.remplirGraph(ConfigTest.get_graph_baisse())
        res.process(actionTest2)
        actionTest2.calculFinalNote()

        self.assertEqual(actionTest2.getFinalNote(), -20)

        # Test 3
        actionTest3.remplirGraph(ConfigTest.get_graph_baisse())
        res.process(actionTest3)
        actionTest3.calculFinalNote()

        self.assertEqual(actionTest3.getFinalNote(), -20)

    def test_process_stable(self):
        actionTest1 = Action("Test1")
        res = Support()

        actionTest1.remplirGraph(ConfigTest.get_graph_stable())
        res.process(actionTest1)
        actionTest1.calculFinalNote()

        # Ne fonctionne pas selon les données du graph
        self.assertEqual(actionTest1.getFinalNote(), 0)

    def test_process_change_for_hausse(self):
        action1 = Action("Test1")
        sup = Support()

        action1.remplirGraph(ConfigTest.get_change_for_hausse())
        sup.process(action1)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), 20)

    def test_process_change_for_baisse(self):
        action1 = Action("Test1")
        sup = Support()

        action1.remplirGraph(ConfigTest.get_change_for_baisse())
        sup.process(action1)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), -20)
