import datetime
import copy
import yfinance as yf

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


@app.route('/testAlgo')
def test_algo():
    actions = list()
    donnees = list()
    classement = list()
    dateDebut = datetime.date(2020, 2, 1)
    dateDebutData = dateDebut - datetime.timedelta(days=200)
    wallet = {'cash': 10000, 'actions': [], 'prixAchat': [], 'nb': [], 'dateAchat': []}
    nbTransaction = 0
    nbJourPossession = []
    possessionMoyenne = 0
    gainTransaction = []
    gainMoyen = 0
    gagnante = 0
    perdante = 0
    resum = ""

    # Requête à la base de données pour récupérer les différentes actions et les instancier
    cursor = mysql.connection.cursor()
    req = "SELECT name, symbol FROM action"
    cursor.execute(req)
    data = cursor.fetchall()
    cursor.close()

    for row in data:
        actions.append(Action(row[0]))
        actions[len(actions) - 1].addSymbol(row[1])
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

        """for action in actions:
            # Récupération des données de l'action sur un an
            graph = yf.Ticker(action.getSymbol() + ".PA").history(start=dateDebutData, end=dateDebut, interval="1d")

            # Tri des données utiles dans une liste de dictionnaires
            for row in graph.itertuples():
                donnees.append({'date': row[0], 'data': [row[1], row[2], row[3], row[4], row[5]]})
                # Data : OpeningPrice, TopPrice, BottomPrice, ClosingPrice, Volume

            action.remplirGraph(copy.deepcopy(donnees))
            donnees.clear()"""

        # Application du pipeline sur les actions
        for j in range(len(actions)):
            Algorithme.Notation(actions[j])

        # Tri des actions
        trieur = Trieur(actions)
        trieur.classer()
        for action in trieur.get_list():
            classement.append({'Nom': action.nom, 'Note': action.getFinalNote()})

        # Stratégie achat-vente
        k = 0
        resum = resum + dateDebut.isoformat() + "<br/>"

        # Stop-loss, vente des actions dont le prix chute sous 5% de la valeur d'achat
        """while k < len(wallet['actions']):
            if wallet['actions'][k].getGraphData()[len(wallet['actions'][k].getGraphData()) - 1]['data'][2] <= (
                    wallet['prixAchat'][k] - wallet['prixAchat'][k] * (5 / 100)):
                wallet['cash'] += wallet['nb'][k] * \
                                  wallet['actions'][k].getGraphData()[len(wallet['actions'][k].getGraphData()) - 1][
                                      'data'][2]

                resum = resum + "Vente des actions " + wallet['actions'][k].getNom() + "<br/>"
                wallet['nb'].pop(k)
                wallet['prixAchat'].pop(k)
                wallet['actions'].remove(wallet['actions'][k])
            else:
                k += 1"""

        k = 0
        # Vente des actions qui perdent de la valeur en fin de semaine
        if dateDebut.strftime('%A') == "Friday":
            while k < len(wallet['actions']):
                if wallet['prixAchat'][k] > \
                        wallet['actions'][k].getGraphData()[len(wallet['actions'][k].getGraphData()) - 1]['data'][3]:
                    wallet['cash'] += wallet['nb'][k] * \
                                      wallet['actions'][k].getGraphData()[len(wallet['actions'][k].getGraphData()) - 1][
                                          'data'][3]

                    resum = resum + "Vente des actions " + wallet['actions'][k].getNom() + "<br/>"

                    nbJourPossession.append((dateDebut - wallet['dateAchat'][k]).days)
                    if wallet['actions'][k].getGraphData()[len(wallet['actions'][k].getGraphData()) - 1]['data'][3] - wallet['prixAchat'][k] > 0:
                        gagnante += 1
                    else:
                        perdante += 1
                    gainTransaction.append(wallet['actions'][k].getGraphData()[len(wallet['actions'][k].getGraphData()) - 1]['data'][3] - wallet['prixAchat'][k])

                    wallet['nb'].pop(k)
                    wallet['prixAchat'].pop(k)
                    wallet['dateAchat'].pop(k)
                    wallet['actions'].remove(wallet['actions'][k])
                    nbTransaction += 1
                else:
                    k += 1

        nbAchats = 10 - len(wallet['actions'])
        achats = 0
        k = 0
        if nbAchats != 0:
            borne = wallet['cash'] / nbAchats
        # Achat d'action qui prennent de la valeur
        while achats < nbAchats and k < 40 and (dateDebut.strftime('%A') not in ["Friday", "Saturday", "Sunday"]):
            if not (trieur.get_list()[k] in wallet['actions']) and (trieur.get_list()[k].getFinalNote() > 0):
                nbActions = 0

                # Calcul du nombre de titre à acheter
                while (nbActions *
                       trieur.get_list()[k].getGraphData()[len(trieur.get_list()[k].getGraphData()) - 1]['data'][
                           0]) <= borne and (nbActions *
                                             trieur.get_list()[k].getGraphData()[
                                                 len(trieur.get_list()[k].getGraphData()) - 1]['data'][
                                                 0]) < wallet['cash']:
                    nbActions += 1

                if nbActions > 0:
                    # Ajout des titres achetés au portefeuille
                    wallet['actions'].append(trieur.get_list()[k])
                    wallet['prixAchat'].append(
                        trieur.get_list()[k].getGraphData()[len(trieur.get_list()[k].getGraphData()) - 1]['data'][0])
                    wallet['nb'].append(nbActions)
                    wallet['dateAchat'].append(dateDebut)
                    wallet['cash'] -= nbActions * \
                                      trieur.get_list()[k].getGraphData()[len(trieur.get_list()[k].getGraphData()) - 1][
                                          'data'][0]

                    nbAchats += 1
                    nbTransaction += 1
                    resum = resum + "Achat de " + nbActions.__str__() + " actions de " + trieur.get_list()[
                        k].getNom() + "<br/>"
            k += 1

        # Valorisatin et pourcentage gain/perte
        val = wallet['cash']
        for j in range(len(wallet['actions'])):
            val += wallet['nb'][j] * \
                   wallet['actions'][j].getGraphData()[len(wallet['actions'][j].getGraphData()) - 1]['data'][3]
        gain = (val - 10000) / 10000 * 100

        # Statistique moyenne sur le nombre de jour de possession d'une action et le gain moyen des transactions
        if len(nbJourPossession) != 0:
            for j in range(len(nbJourPossession)):
                possessionMoyenne += nbJourPossession[j]
            possessionMoyenne = possessionMoyenne / len(nbJourPossession)

        if len(gainTransaction) != 0:
            for j in range(len(gainTransaction)):
                gainMoyen += gainTransaction[j]
            gainMoyen = gainMoyen/len(gainTransaction)

        # Résumé des statistiques pour affichage
        resum = resum + "Valorisation à la fin de la journée : " + "{:.2f}".format(val) + "€<br/>"
        resum = resum + "Pourcentage gain/perte depuis le début : " + "{:.2f}".format(gain) + "%<br/>"
        resum = resum + "Nombre de transaction depuis le début : " + "{:.2f}".format(nbTransaction) + "<br/>"
        resum = resum + "Gain moyen par transaction : " + "{:.2f}".format(gainMoyen) + "<br/>"
        resum = resum + "Nombre de transaction gagnante : " + "{:.2f}".format(
            gagnante) + ", Nombre de transaction perdante " \
                        ": " + "{:.2f}".format(perdante) + \
                "<br/> "
        resum = resum + "Nombre de jour moyen de possession : " + "{:.2f}".format(possessionMoyenne) + "<br/>"

        resum = resum + "<br/>"

    # return jsonify(classement)
    return resum


@app.route('/main')
def main():
    actions = list()
    donnees = list()
    classement = list()

    # Requête à la base de données pour récupérer les différentes actions et les instancier
    cursor = mysql.connection.cursor()
    req = "SELECT name, symbol FROM action"
    cursor.execute(req)
    data = cursor.fetchall()
    cursor.close()

    for row in data:
        actions.append(Action(row[0]))
        actions[len(actions) - 1].addSymbol(row[1])
    actions.remove(actions[0])  # Retire la première ligne qui contient les noms des colonnes

    # Récupération des données
    for action in actions:
        # Récupération des données de l'action sur un an
        graph = yf.Ticker(action.getSymbol() + ".PA").history(period="1y", interval="1d")

        # Tri des données utiles dans une liste de dictionnaires
        for row in graph.itertuples():
            donnees.append({'date': row[0], 'data': [row[1], row[2], row[3], row[4], row[5]]})
            # Data : OpeningPrice, TopPrice, BottomPrice, ClosingPrice, Volume

        action.remplirGraph(copy.deepcopy(donnees))
        donnees.clear()

    # Application du pipeline sur les actions
    for i in range(len(actions)):
        Algorithme.Notation(actions[i])

    # Tri des actions
    trieur = Trieur(actions)
    trieur.classer()
    for action in trieur.get_list():
        classement.append({'Nom': action.nom, 'Note': action.getFinalNote()})

    return jsonify(classement)


@app.route('/testData')
def testData():
    actions = list()
    donnees = list()

    # Requête à la base de données pour récupérer les différentes actions et les instancier
    cursor = mysql.connection.cursor()
    req = "SELECT name, symbol FROM action"
    cursor.execute(req)
    data = cursor.fetchall()
    cursor.close()

    for row in data:
        actions.append(Action(row[0]))
        actions[len(actions) - 1].addSymbol(row[1])
    actions.remove(actions[0])  # Retire la première ligne qui contient les noms des colonnes

    # Récupération des données
    for action in actions:
        # Récupération des données de l'action sur un an
        graph = yf.Ticker(action.getSymbol() + ".PA").history(period="1y", interval="1d")

        # Tri des données utiles dans une liste de dictionnaires
        for row in graph.itertuples():
            donnees.append({'date': row[0], 'data': [row[1], row[2], row[3], row[4], row[5]]})
            # Data : OpeningPrice, TopPrice, BottomPrice, ClosingPrice, Volume

        action.remplirGraph(copy.deepcopy(donnees))
        donnees.clear()

    return jsonify(actions[len(actions) - 1].getGraphData())


if __name__ == '__main__':
    app.run()
