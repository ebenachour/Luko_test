# Luko_test
#####
ENONCÉ:

On te propose de passer un peu de temps et de réflexion sur un sujet récurrent chez nous, qui est la gestion de notre data élec en base de donnée Timeserie. 

Le but c'est de réfléchir à une solution pour répondre à nos 3 besoins sur la data élec: 

	1. pour que les utilisateurs puissent voir combien ils consomment chez eux tout de suite : montrer la conso électrique live, pour chaque capteur

	2. envoyer la conso électrique du mois dernier, agrégée à la minute, tous les jours à minuit, à un partenaire. En retour on reçoit un découpage des usages (20% de la conso est partie dans ton chauffe eau, 10% dans le frigo, etc...) à aussi montrer à l'utilisateur.

	3. montrer la conso électrique historique (des 3 dernières années), agrégée au quart d'heure, la aussi depuis une app, pour chaque capteur. Les utilisateurs vont visualiser cette donnée pour savoir combien ils ont consommé dans la semaine, le mois... Et pour comparer avec leur conso du mois / de l'année dernière.

Je te propose la démarche suivante (mais sens toi assez libre de faire ça comme bon te semble) :

- Mettre en place une BDD Timeseries, en docker local, ou sur un cloud
Nous on utilise InfluxDB, qui a une bonne doc pour une installation sur AWS (attention au coût par contre) https://docs.influxdata.com/influxdb/v1.7/introduction/installation/#hosting-influxdb-oss-on-aws. Il paraît que Prometheus est pas mal aussi à l'utilisation.

- Construire un set de data à la seconde, sur 3 mois, qui proviendrait de plusieurs capteurs différents. 
Tu peux peut être trouver quelque chose d'intéressant en open data: https://www.data.gouv.fr/fr/, https://msropendata.com/datasets, https://ai.google/tools/datasets/ Mais sinon de la data random ira très bien.

- Stocker cette donnée dans ta DB. Si en plus de la data 3 mois, tu arrives à faire que de la donnée live continue à être écrite à la seconde en stream entrant, c'est génial.

- Trouver une stratégie pour générer les données minutes et quart d'heure à de bonnes fréquences pour leur utilisation (on appelle ça du down-samplig), et les stocker à nouveau dans ta DB.

- Visualiser cette data pour répondre aux besoins donnés au début.


#




##### Debut de réponse:

a) Installation de l'infrastructure
Choix techniques:
  - Grafana : visualisation des données
  - influxdb: Base de données timeseries
  - Telegraf: Pour envoyer la data vers influxdb
  - Importer: Dossier contenant le Script python pour mettre en place de la données sur 3 mois (docker python 3.7) 

Docker-compose avec Grafana et influxdb.
Telegraf installé depuis les sources. 
connexion sur  localhost:3000 puis configuration manuelle de grafana, connexion avec influxdb ...
configuration de telegraf. (on a pris les outputs disk et cpu pour l'instant pour tester).

To be continued

