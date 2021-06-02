from unittest import TestCase
from models.Action import Action
from pipeAndFilter.filters.MoyenneExponentielle import MoyenneExponentielle
from tools.ConfigTest import ConfigTest


class TestMoyenneExponentielle(TestCase):
    """Classe de test ATTENTION : la MACD a un fort potentiel de faux signaux, il ne faut pas se fier qu'à cet
    indicateur test fail une fois sur deux si on recherche une valeur strictement positive ou strictement négative
    sur une tendance fixe """

    def test_process_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        me = MoyenneExponentielle()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_hausse())
        me.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() != 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_hausse())
        me.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action2.getFinalNote() != 0)

    def test_process_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        me = MoyenneExponentielle()

        # Test 1
        action1.remplirGraph(ConfigTest.get_graph_baisse())
        me.process(action1)
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() != 0)

        # Test 2
        action2.remplirGraph(ConfigTest.get_graph_baisse())
        me.process(action2)
        action2.calculFinalNote()

        self.assertTrue(action2.getFinalNote() != 0)

    def test_process_change_for_hausse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        me = MoyenneExponentielle()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_hausse())
        me.process(action1)
        action1.calculFinalNote()

        self.assertTrue(6 <= action1.getFinalNote() <= 34)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_hausse())
        me.process(action2)
        action2.calculFinalNote()

        self.assertTrue(6 <= action2.getFinalNote() <= 34)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_hausse())
        me.process(action3)
        action3.calculFinalNote()

        self.assertTrue(6 <= action3.getFinalNote() <= 34)

    def test_process_change_for_baisse(self):
        action1 = Action("Test1")
        action2 = Action("Test2")
        action3 = Action("Test3")
        me = MoyenneExponentielle()

        # Test 1
        action1.remplirGraph(ConfigTest.get_change_for_baisse())
        me.process(action1)
        action1.calculFinalNote()

        self.assertTrue(-34 <= action1.getFinalNote() <= -6)

        # Test 2
        action2.remplirGraph(ConfigTest.get_change_for_baisse())
        me.process(action2)
        action2.calculFinalNote()

        self.assertTrue(-34 <= action2.getFinalNote() <= -6)

        # Test 3
        action3.remplirGraph(ConfigTest.get_change_for_baisse())
        me.process(action3)
        action3.calculFinalNote()

        self.assertTrue(-34 <= action3.getFinalNote() <= -6)
