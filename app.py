import datetime
import copy

from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL
from models.Action import Action
from tools.Algorithme import Algorithme
from tools.Trieur import Trieur

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'api'

mysql = MySQL(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/displayGraphData')
def display_graph_data():
    action = Action("Atos")

    # Requête à la base de données pour récupérer les informations de l'action
    cursor = mysql.connection.cursor()
    req = "SELECT * from days JOIN action USING(idAction) WHERE name like '%" + action.nom + "%' and date > '2020-01-01'"
    cursor.execute(req)
    data = cursor.fetchall()
    cursor.close()

    donnees = []
    # On remplit le dictionnaire des données de l'action sur la période considérée
    for row in data:
        donnees.append({'date': row[1], 'data': [row[2], row[3], row[4], row[5], row[6]]})
        # Data : OpeningPrice, TopPrice, BottomPrice, ClosingPrice, Volume

    action.remplirGraph(donnees)

    return jsonify(action.getGraphData())


@app.route('/test')
def test():
    return


@app.route('/testAlgo')
def test_algo():
    actions = list()
    donnees = list()
    classement = list()
    dateDebut = datetime.date(2020, 1, 1)
    dateDebutData = dateDebut - datetime.timedelta(days=200)

    # Requête à la base de données pour récupérer les différentes actions et les instancier
    cursor = mysql.connection.cursor()
    req = "SELECT name FROM action"
    cursor.execute(req)
    data = cursor.fetchall()
    cursor.close()

    for row in data:
        actions.append(Action(row[0]))
    actions.remove(actions[0])  # Retire la première ligne qui contient les noms des colonnes

    # Boucle de test d'achat-vente sur une certaine période
    for i in range(30):
        # Jour suivant, reset des données
        dateDebutData = dateDebutData + datetime.timedelta(days=1)
        dateDebut = dateDebut + datetime.timedelta(days=1)
        classement.clear()
        for action in actions:
            action.resetNote()

        # Requête à la base de données pour récupérer les informations des actions
        for j in range(len(actions)):
            cursor = mysql.connection.cursor()
            req = "SELECT * FROM days JOIN action USING(idAction) WHERE name like '%" + actions[
                j].getNom() + "%' and date between '" + dateDebutData.isoformat() + "' and '" + dateDebut.isoformat() + "'"
            cursor.execute(req)
            data = cursor.fetchall()
            cursor.close()

            # On remplit le dictionnaire des données de l'action sur la période considérée
            for row in data:
                donnees.append({'date': row[1], 'data': [row[2], row[3], row[4], row[5], row[6]]})
                # Data : OpeningPrice, TopPrice, BottomPrice, ClosingPrice, Volume

            actions[j].remplirGraph(copy.deepcopy(donnees))
            donnees.clear()

        # Application du pipeline sur les actions
        for j in range(len(actions)):
            Algorithme.Notation(actions[j])

        # Tri des actions
        trieur = Trieur(actions)
        trieur.classer()
        # classement = trieur.get_list()
        for action in trieur.get_list():
            classement.append({'Nom': action.nom, 'Note': action.getFinalNote()})

        # Stratégie achat-vente

    return jsonify(classement)


if __name__ == '__main__':
    app.run()
