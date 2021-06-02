# API de prédiction boursière sur les actions du CAC40

## L'API applique un algorithme sur les différentes actions du cac40 et leur donne une note. Les actions sont ensuites classées par ordre décroissant.

### Fonctionnement de l'API
Au lancement de l'API, l'application lance la procédure statique de notation de la classe Algorithme. Celle-ci va instancier le pipeline ainsi que les classes représentant les différents filtres. Elle va ensuite ajouter chaque filtre au pipeline puis exécuter ce dernier. Celui-ci exécute les procédures d'exécution des filtres séparéments. Ceux-ci attribuent chacun une note à l'action sur laquelle il est appliqué. Après arrêt du pipeline, la note finale de l'action est calculée en additionnant toutes les notes obtenues par les différents filtres.

A la fin de l'algorithme de notation, les actions sont classées par ordre décroissant des notes par la classe Trieur, qui retourne ensuite la nouvelle liste triée.

### Exécution en local
Pour exécuter les fichiers de tests en local, il faut juste lancer l'exécution du fichier voulu : "run unittest in file"

Pour exécuter le fichier principal app.py, il faut un environnement web avec localhost et la base de donnée de l'API.
Une fois l'environnement prêt, il suffit de lancer l'application en local, celle-ci doit s'ouvrir dans le localhost.
Puis on ajoute à l'url le chemin qui permet d'exécuter la fonction souhaitée.
La fonction test retourne le résultat de simulation sous forme texte dans le navigateur.
La fonction principale main de l'API retourne le résultat de l'algorithme sous la forme d'un fichier JSON.

### Package Python nécessaire à l'API
* flask
* mysql
* mysql-connector-python
* Flask-MySQLdb

### Extension nécessaire à l'exécution des tests
* Unittests

### Extension nécessaire à l'exécution en local
* mysqlclient

### Package du repository
* models
    *Classe Action et Graph : nécessaire à la description d'une action*
* pipeAndFilter
    *Classe Pipeline, qui crée le pipeline pour l'exécution en pipe and filter*
    * filters
        *Ensemble des classes qui correspondent aux filtres de l'application*
* tools
    *Classes outils : Algorithme, Trieur, ConfigTest*
* tests
    *Ensemble des tests des classes de l'application*