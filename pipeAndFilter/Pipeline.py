import types


class Pipeline:
    filtres: []  # Liste des filtres du pipeline

    """
    @param self: objet de la classe
    """
    def __init__(self):
        self.filtres = list()

    """
    @param self: objet de la classe
    @param filter: Filtre à ajouter au pipeline
    """
    def addFilter(self, filter):
        self.filtres.extend(filter)

    """
    @param self: objet de la classe
    @param action: Action sur laquelle le pipeline est appliqué
    """
    def execute(self, action):
        # On parcourt la liste des filtres et on les applique à l'action
        for f in self.filtres:
            if type(f) == types.FunctionType:
                f(action)
            else:
                f.process(action)

    """
    @param self: objet de la classe
    """
    def filterLen(self):
        return len(self.filtres)
