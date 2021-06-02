from unittest import TestCase
from models.Action import Action
from tools.Trieur import Trieur


class TestTrieur(TestCase):
    def test_add_action(self):
        action1 = Action("ALO")
        action2 = Action("COQ")
        action3 = Action("CHAT")

        trieur = Trieur([])

        trieur.addAction(action1)
        trieur.addAction(action2)
        trieur.addAction(action3)

        self.assertEqual(len(trieur.actions), 3)

    def test_classer(self):
        action1 = Action("ALO")
        action1.addNote(50)
        action1.calculFinalNote()

        action2 = Action("COQ")
        action2.addNote(5)
        action2.calculFinalNote()

        action3 = Action("CHAT")
        action3.addNote(25)
        action3.calculFinalNote()

        trieur = Trieur([])

        trieur.addAction(action1)
        trieur.addAction(action2)
        trieur.addAction(action3)

        trieur.classer()

        self.assertTrue(trieur.actions[0] is action2)
        self.assertTrue(trieur.actions[1] is action3)
        self.assertTrue(trieur.actions[2] is action1)

        action4 = Action("SAO")
        action4.addNote(-20)
        action4.calculFinalNote()

        action5 = Action("Nya")
        action5.addNote(-5)
        action5.calculFinalNote()

        trieur.addAction(action4)
        trieur.addAction(action5)

        trieur.classer()
        liste = trieur.get_list()

        self.assertTrue(liste[0] is action4)
        self.assertTrue(liste[1] is action5)
        self.assertTrue(liste[4] is action1)

    def test_get_list(self):
        action1 = Action("ALO")
        action2 = Action("COQ")
        action3 = Action("CHAT")

        trieur = Trieur([])

        trieur.addAction(action1)
        trieur.addAction(action2)
        trieur.addAction(action3)

        liste = trieur.get_list()

        self.assertTrue(liste is not None and len(liste) == 3)
