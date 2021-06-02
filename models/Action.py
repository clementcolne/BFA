from Graph import Graph


class Action:
    nom: str
    symbol = str
    graph: Graph
    notes: []
    finalNote: int

    '''
    @param self: objet de cette classe
    @param name: nom de l'action
    '''
    def __init__(self, name):
        self.nom = name
        self.graph = Graph()
        self.notes = []
        self.finalNote = 0

    '''
    @param sef: objet de cette classe
    @param n: note à ajouter à l'action
    '''
    def addNote(self, n):
        self.notes.append(n)

    '''
    @param self: objet de cette classe
    @return Longueur du tableau des notes
    '''
    def getNotesLen(self):
        return len(self.notes)

    '''
    @param self: objet de la classe
    '''
    def calculFinalNote(self):
        for n in self.notes:
            self.finalNote += n

    '''
    @param self: objet de la classe
    @return La note finale de l'action
    '''
    def getFinalNote(self):
        return self.finalNote

    '''
    @param self: objet de la classe
    @param donnees: Liste des données graphiques de l'action
    '''
    def remplirGraph(self, donnees):
        self.graph.remplirGraph(donnees)

    '''
    @param self: objet de la classe
    @return Les données graphiques de l'action
    '''
    def getGraphData(self):
        return self.graph.getData()

    '''
    @param self: objet de la classe
    @return Le nom de l'action
    '''
    def getNom(self):
        if self.nom.__contains__("'"):
            name = self.nom.split("'")
            return name[0] + "''" + name[1]
        return self.nom

    '''
    @param self: objet de la classe
    '''
    def resetNote(self):
        self.notes.clear()
        self.finalNote = 0

    '''
    @param self: objet de la classe
    @param s : symbole de l'action
    '''
    def addSymbol(self, s):
        self.symbol = s

    '''
    @param self: objet de la classe
    @return Symbole de la classe
    '''
    def getSymbol(self):
        return self.symbol
