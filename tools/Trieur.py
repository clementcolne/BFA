from operator import attrgetter


class Trieur:
    actions: []

    """
    @param self: objet de la classe
    @param actions: Ensemble d'actions à trier
    """
    def __init__(self, actions):
        self.actions = actions

    """
    @param self: objet de la classe
    @param action: Action à ajouter au trieur
    """
    def addAction(self, action):
        self.actions.append(action)

    """
    @param self: objet de la classe
    """
    def classer(self):
        self.actions = sorted(self.actions, key=attrgetter('finalNote'))

    """
    @param self: objet de la classe
    @return La liste des actions du trieur
    """
    def get_list(self):
        return self.actions
