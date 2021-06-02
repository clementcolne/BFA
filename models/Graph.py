class Graph:
    data: []

    '''
    @param self: objet de la classe
    '''
    def __init__(self):
        self.data = []

    '''
    @param self: objet de la classe
    @param donnees: Données graphique d'une action
    '''
    def remplirGraph(self, donnees):
        self.data = donnees

    '''
    @param self: objet de la classe
    @return Les données graphiques d'une action
    '''
    def getData(self):
        return self.data
