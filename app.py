import datetime

from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL
from models.Action import Action

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

    #Requête à la base de donnée pour récupérer les informations de l'action
    cursor = mysql.connection.cursor()
    req = "SELECT * from days JOIN action USING(idAction) WHERE name like '%" + action.nom + "%' and date > '2020-01-01'"
    cursor.execute(req)
    data = cursor.fetchall()
    cursor.close()

    donnees = []
    # On remplit le dictionnaire des données de l'action sur la période considérée
    for row in data:
        donnees.append({'date': row[1], 'data': [row[2], row[3], row[4], row[5], row[6]]})
        #Data : OpeningPrice, TopPrice, BottomPrice, ClosingPrice, Volume

    action.remplirGraph(donnees)

    return jsonify(action.getGraphData())


if __name__ == '__main__':
    app.run()
