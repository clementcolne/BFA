from unittest import TestCase
from models.Action import Action


class TestAction(TestCase):
    def test_add_note(self):
        # Premier test
        action1 = Action("RMS")

        action1.addNote(10)
        action1.addNote(10)
        action1.addNote(10)
        self.assertTrue(action1.getNotesLen() == 3)
        self.assertFalse(action1.getNotesLen() == 0)
        self.assertFalse(action1.getNotesLen() == 2)

        # Second test
        action2 = Action("ALO")

        action2.addNote(5)
        self.assertTrue(action2.getNotesLen() == 1)
        self.assertFalse(action2.getNotesLen() == 2)
        self.assertFalse(action2.getNotesLen() == 0)

    def testGetFinalNote(self):
        # Premier test
        action1 = Action("RMS")

        action1.addNote(10)
        action1.addNote(5)
        action1.addNote(20)
        action1.calculFinalNote()

        self.assertEqual(action1.getFinalNote(), 35)

        # Second test
        action2 = Action("ALO")

        action2.addNote(20)
        action2.addNote(30)
        action2.calculFinalNote()

        self.assertEqual(action2.getFinalNote(), 50)

        # Troisième test
        action3 = Action("ORA")

        action3.addNote(10)
        action3.addNote(30)
        action3.addNote(5)
        action3.addNote(2)
        action3.addNote(9)
        action3.calculFinalNote()

        self.assertEqual(action3.getFinalNote(), 56)

        # Quatrième test
        action4 = Action("CA")

        action4.addNote(50)
        action4.addNote(-10)
        action4.addNote(-20)
        action4.addNote(5)
        action4.calculFinalNote()

        self.assertEqual(action4.getFinalNote(), 25)
