class Graph:
    data: []

    """Constructeur de Graph"""

    def __init__(self):
        self.data = []

    """Procédure de remplissage du graph
    @:param donnees les informations du graph"""

    def remplirGraph(self, donnees):
        self.data = donnees

    """Fonction qui récupère les données du graph"""
    def getData(self):
        return self.data
