class Pipeline:
    filtres: []  # Liste des filtres du pipeline

    """Constructeur de la classe Pipeline"""

    def __init__(self):
        self.filtres = list()

    """Procédure d'ajout d'un filtre dans le pipeline
    @:param filter le filtre à ajouter au pipeline"""

    def addFilter(self, filter):
        self.filtres.extend(filter)

    """Procédure d'exécution du pipe and filter
    @:param action l'action sur laquelle on exécute le pipe and filter"""

    def execute(self, action):
        # On parcourt la liste des filtres et on les applique à l'action
        for f in self.filtres:
            f(action)

    """Fonction qui récupère le nombre de filtres dans le pipeline"""

    def filterLen(self):
        return len(self.filtres)
