from Graph import Graph
from app import app
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'api'

mysql = MySQL(app)


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

    def remplirGraph(self, dateDebut, dateFin):
        # Récupération des données du graph dans la base de données
        cursor = mysql.connection.cursor()
        cursor.execute(
            '''SELECT * FROM days WHERE name = ''' + self.nom + '''and (date between ''' + dateDebut + ''' and ''' + dateFin + ''')''') # Modifier la requête par id, pas par nom
        data = cursor.fetchall()
        cursor.close()
        donnees = dict()

        # On remplit le dictionnaire des données de l'action sur la période considérée
        for row in data:
            donnees['date': row[0]] =\
                {'OpeningPrice': row[1], 'TopPrice': row[2], 'BottomPrice': row[3], 'ClosingPrice': row[4]}

        # On donne les données au graph
        self.graph.remplirGraph(donnees)
