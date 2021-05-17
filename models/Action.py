from Graph import Graph
from flask_mysqldb import MySQL


class Action:
    nom: str
    graph: Graph
    notes: []
    finalNote: int

    """Constructeur de la classe Action
    @:param name nom de l'action"""

    def __init__(self, name):
        self.nom = name
        self.graph = Graph()
        self.notes = []
        self.finalNote = 0

    """Procédure qui ajoute une note à l'action
    @:param n note à ajouter"""

    def addNote(self, n):
        self.notes.append(n)

    """Fonction qui récupère le nombre de notes données à l'action"""

    def getNotesLen(self):
        return len(self.notes)

    """Procédure de calcul de la note final une fois le tableau des notes remplis"""

    def calculFinalNote(self):
        for n in self.notes:
            self.finalNote += n

    """Fonction pour récupérer la note finale après son calcul"""

    def getFinalNote(self):
        return self.finalNote

    """Procédure qui récupère les informations du graph en base de données afin de le remplir
    @:param dateDebut date de début des informations à récupérer
    @:param dateFin date de fin des informations à récupérer"""

    def remplirGraph(self, donnees):
        self.graph.remplirGraph(donnees)

    """Fonction pour récupérer les données du graph"""
    def getGraphData(self):
        return self.graph.getData()

    """Fonction pour récupérer le nom de l'action"""
    def getNom(self):
        if self.nom.__contains__("'"):
            name = self.nom.split("'")
            return name[0] + "''" + name[1]
        return self.nom
