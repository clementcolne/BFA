from unittest import TestCase
from models.Action import Action
from pipeAndFilter.filters.Stochastique import Stochastique
from tools.ConfigTest import ConfigTest


class TestStochastique(TestCase):
    def test_process_hausse(self):
        action1 = Action("Test1")
        sto = Stochastique()

        action1.remplirGraph(ConfigTest.get_graph_hausse())
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() == 0)

    def test_process_baisse(self):
        action1 = Action("Test1")
        sto = Stochastique()

        action1.remplirGraph(ConfigTest.get_graph_baisse())
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() == 0)

    def test_process_stable(self):
        action1 = Action("Test1")
        sto = Stochastique()

        action1.remplirGraph(ConfigTest.get_graph_stable())
        action1.calculFinalNote()

        self.assertTrue(action1.getFinalNote() == 0)

    # Note : ajouter une config de test avec un graph plus mouvementé pour tester le Stochastique
