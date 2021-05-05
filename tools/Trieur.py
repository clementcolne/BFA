from operator import attrgetter


class Trieur:
    actions: []

    """Constructeur du Trieur
    @:param actions la liste des actions"""

    def __init__(self, actions):
        self.actions = actions

    """Procédure d'ajout d'une action dans le trieur
    @:param action l'action à ajouter"""

    def addAction(self, action):
        self.actions.append(action)

    """Procédure de classement des actions selon leur note"""

    def classer(self):
        self.actions = sorted(self.actions, key=attrgetter('finalNote'))

    """Fonction qui récupère la liste des actions
    @:return la liste des actions"""

    def get_list(self):
        return self.actions
