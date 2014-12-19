Compte-rendu des conférences : Pélican et (i)Python
####################################################

:date: 2014-12-04
:tags: pelican,travis,ipython,dataviz,cartographie
:category: comptes-rendus
:author: Pierre, Gordon, Florent
:email: twildawnight@gmail.com, damien@gordon.re, florentlebreton@free.fr
:summary: Compte-rendu du meetup/conférence du 18 novembre 2014

Un meetup tardif, dû à la PyConFr, centré sur deux présentations opposées en
termes de technicité : une présentation d’un outil (presque) clés-en-mains, et
un survol des possibilités de iPython dans la dataviz cartographique, ainsi que
quelques bibliothèques utiles.

==============================================================================
Pelican : le futur du web vintage
==============================================================================

Intervenant : Damien Nicolas, Gordon

Principe
--------
Pelican est un générateur de site statique écrit en Python initialement par Alexis Métaireau.

Le site est réalisé via un langage de template ensuite traduit en HTML. Le contenu généré peut ensuite être déployé sur un serveur sans configuration supplémentaire. Il n’y a donc pas d’applicatif sur le serveur.

Les avantages d’un tel système sont nombreux. D’abord la simplicité. Un simple éditeur de texte suffit pour écrire le contenu. Étant purement textuel, le contenu est facilement versionnable et recevoir/fournir un patch peut se résumer à un envoi de mail. L'absence d’applicatif côté serveur rend la configuration serveur aisée et la sécurité proche de la perfection : pas d’applicatif = pas de faille.

Bon évidemment, il y a quelques inconvénients. En terme de fonctionnalité d’abord, l’absence native de recherche ou de commentaire. Mais heureusement, il est possible via des extensions de remédier à ces problèmes.
En revanche, la barrière à l’entrée est immuable. Pour faire du Pelican, il faut pouvoir écrire du RestructuredText ou du Markdown. Pour profiter pleinement de tout ça, il est bon de savoir invoquer une commande “make” ou “git push”. Plus que rébarbatif pour un néophyte.

En pratique
-----------
L’installation se fait comme n’importe quelle bibliothèque Python. On crée un environnement virtuel (e.g. via pyvenv en Python 3). On l’active et via pip on peut installer Pelican. A noter que par défaut, Pelican supporte uniquement le RestructuredText pour les articles, pour markdown, il faudra installer le paquet markdown en plus.
On peut ensuite préparer le site via l'installer de Pelican, qui de façon interactive pose quelques questions qui facilitent grandement la configuration. A cette étape, on paramètre notamment les différents moyens utiliser pour déployer le site web sur le serveur.

Une fois configuré, on peut écrire des articles. Ces derniers pourront être placés dans un dossier **articles** dans le dossier **content** (tout ceci est paramétrable). Pour générer le site, le plus simple est d'utiliser la commande make :

.. code::

    make html

Et on déploie :

.. code::

    make upload

Et la magie opère. Le site est redéployé !

Il est assez facile de tester localement, Pelican permet d’utiliser un simple serveur HTTP en local pour vérifier ses modifications avant de publier des erreurs ;).

Extensions
----------

On l’a écrit, nativement, il n’existe pas de gestion des commentaires 
ni de fonction de recherche. Rien d’insurmontable cependant.

Commentaires
`````````````
Pour les commentaires, une solution simple est d’intégrer `Disqus <https://github.com/Python-Nairobi/pelican-plugins/tree/master/disqus>`_. Disqus est un service permettant de stoquer des commentaires sur un autre serveur que celui de l’application. L’extension disqus_static permet d’utiliser l’API de ce service pour gérer les commentaires dans Pelican. Il y a d’autres alternatives, comme par exemple gérer des commentaires statiquement dans des fichiers sur le serveur hébergeant Pelican. Cette dernière solution permet d’éviter les dépendances à un service tiers.

Recherche
`````````
Ici, on pourra fait appel à `tipue_search <http://www.tipue.com/search/>`_, qui permet d’intégrer une fonctionnalité de recherche côté client. Sur le serveur, un fichier JSON est généré. Celui-ci est ensuite utilisé côté client pour de la recherche via JQuery. Le thème ``elegant`` intègre cette fonctionnalité nativement.

Autres extensions
```````````````````
Très extensible, il est possible de faire tout un tas de choses avec Pelican. C’est d’ailleurs le moteur utilisé pour le blog que vous lisez en ce moment. Pour vous faire une idée des possibilités, c’est par là : <https://github.com/Python-Nairobi/pelican-plugins>`_.

Les slides de la présentation sont disponibles ici : `Pelican </presentations/pelican/pelican-meetup-python.pdf>`_

==============================================================================
Dataviz avec iPython
==============================================================================

Intervenant : Thomas Gratier

IPython est un shell Python interactif offrant autocomplétion et historique des commandes. Il peut également s’utiliser sous forme de notebook dans un navigateur. De nombreuses bibliothèques sont disponibles et peuvent être chargées dynamiquement. Ainsi, il est très aisé de préparer des présentations dynamiques avec démonstration Python en temps réel et image générée directement dans un navigateur. IPython permet aussi de déployer les notebooks sur un site web. C’est donc un outil très puissant à la fois pour expérimenter avec Python mais aussi pour préparer des présentations interactives.

Pas plus de mots, lors du meetup, nous avons pu voir des résultats assez chouettes que vous invités à expérimenter par vous-même ici : `Dataviz avec iPython <http://nantes.afpy.org/presentations/ipython_par_exemple/Ipython_par_l_exemple.html>`_.

Merci à tous pour votre présence et à très bientôt :) !