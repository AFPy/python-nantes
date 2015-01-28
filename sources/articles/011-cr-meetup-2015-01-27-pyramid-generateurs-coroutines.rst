Compte-rendu des conférences : Pyramid, Générateurs et co-routines
##################################################################

:date: 2015-01-27
:tags: pyramid, générateur, co-routine
:category: comptes-rendus
:author: Florent Lebreton
:email: florentlebreton@free.fr
:summary: Compte-rendu de la présentation de Pyramid par Gaël et de l'intervention sur les générateurs et les co-routines de Hugo.

Pour ce premier meetup de janvier, deux sujets ont été présentés devant une quarantaine de personnes visiblement intéressées et attentives. Vous trouverez dans cet article un résumé de ce qui a été proposé, ainsi que les liens vers les présentations.

==============================================================================
Pyramid
==============================================================================

Intervenant : Gaël

Pyramid est un framework web développé en Python. On peut le classer entre Bottle (plus minimaliste) et Django (plus gros et plus monolithique).
Il est nativement WSGI, facilement extensible et laisse beaucoup de souplesse dans les choix techniques et la conception.

Vous verrez dans les slides qu'un classique "Hello World", servi en HTTP, est très simple à réaliser.

Le premier composant à appréhender est le `configurateur <http://docs.pylonsproject.org/docs/pyramid/en/latest/api/config.html>`_, qui permet de configurer une application Pyramid (et notamment de gérer les routes).

Le *routeur* a la particularité de pouvoir fonctionner de `deux manière différentes <http://pyramid-cookbook.readthedocs.org/en/latest/routing/>`_ :

* par mapping des URLs sur des vues 
* en mode *traversal* (les différents fragments de l'URL permettent traverser des classes).

Le routeur permet aussi classiquement de faire de la résolution d'URL, ce qui évite à avoir à répéter des URLs dans les templates par exemple.

Un autre concept assez intéressant du framework est l'utilisation des exceptions. Il est notamment possible de lever des exceptions HTTP ce qui permet de gérer les erreurs sous forme de codes du protocole HTTP (500, 403).

Le concept de *factory* permet de récupérer/travailler sur un objet avant qu'une vue ne soit invoquée, ce qui rend le code de la vue plus simple. Une *factory* peut être factorisée et utilisée dans plusieurs vues.

Le rendu d'une vue se fait via par l'intermédiaire d'une *renderer* et une vue peut être associée à plusieurs renderer (par exemple un rendu json et un rendu HTML via une template). On pourrait aussi avoir plusieurs renderers utilisant des moteurs de templates différents (Chameleon, Jinja, Mako, ...). Il est aussi possible de créer son propre renderer (par exemple pour renvoyer un fichier csv, un pdf, ...).

Le concept de *tween* permet d'intercepter une requête, puis la réponse pour analyser ou modifier l'une ou l'autre. Un cas pratique classique est l'utilisation d'une barre de debuggage permettant d'analyser le comportement de l'application.

Un système d'évènements permet d'associer une fonction à un évènement. Par exemple : ``BeforeRender`` est déclenché avant le rendu d'une template et laisse la possibilité d'injecter des données dans le context passé à la template.

Par ailleurs, Pyramid est modulaire et peut être facilement étendu via la fonction magique ``includeme``. Il est aussi possible d'étendre l'objet ``request`` pour lui ajouter des méthodes par exemple, ce qui peut s'avérer pratique dans certains cas.

Beaucoup de modules supplémentaires sont fournis nativement :

* Gestion de l'authentification et d'autorisations
* Gestion et service des fichiers statiques
* Gestion des sessoins
* Gestion du cache HTTP
* Gestion de prédicats de vue
* Gestion de trasaction étendue (par exemple pour éviter un envoi de mail si une requête SQL a précédemment échoué)
* ...

L'écosystème de Pyramid est assez riche et varié ; plus de 250 packages sont indiqués comme étant compatibles Pyramid sur pypi.

Il existe entre autres des CMS basés sur Pyramid : notamment `substanced <http://substanced.net/>`_ (basé sur la ZODB) et `kotti <http://kotti.pylonsproject.org/>`_.

Les slides de la présentation sont disponibles ici : `Présentation de Pyramid <http://nantes.afpy.org/presentations/pyramid>`_

==============================================================================
Générateurs et coroutines
==============================================================================

Intervenant : Hugo

Les itérateurs / iterables
--------------------------

Le concept d'itérable est simplement une généralisation du concept de séquence ou de liste. Un itérable est défini par le fait qu'il est possible d'itérer dessus, par exemple dans une boucle for ...
La syntaxe [] permet de définir ce qu'on appelle une liste *en compréhension*. L'iterable est un concept pratique mais il a le défaut de stocker tous ses éléménts en mémoire.

Les générateurs
---------------

Un générateur est un itérable qui a la particularité de générer les résultats à la volée. Syntaxiquement une *expression génératrice* peut s'écrire de la même manière qu'un itérable classique, en remplaçant les [] par des ().

Dans un générateur, on utilise le mot clé ``yield`` à la place de ``return``. La première différence est que l'appel de la fonction renverra non pas un résultat mais un générateur, sans que la fonction soit exécutée. La fonction est exécutée à partir du moment où on itère sur le générateur. Le premier appel à la méthode ``next`` permet d'exécuter la fonction jusq'au premier ``yield``. À l'exécution du ``yield``, le générateur rend la main à la fonction appelante et s'arrête (mais l'état de son exécution est enregistré). Dans la fonction appelante, chaque appel de la méthode ``next`` relance donc une exécution du générateur, de l'état où il s'était arrêté jusqu'au ``yield`` suivant.


Plusieurs intérêts notables :

* l'évaluation paresseuse limite l'allocation mémoire
* elle permet aussi de travailler avec une vision "flux de données" (en chainant plusieurs générateurs comme on chaine des commandes unix par exemple ``cat foo.txt | grep bar``)
* possibilité de faire du pseudo-asynchrone de manière synchrone


Les co-routines
---------------

Une co-routine est à peu prêt la même chose qu'un générateur à la différence près qu'elle dispose d'une méthode supplémentaire ``send`` qui permet à la fonction appelante d'envoyer des données à la co-routine. Cela permet d'influer sur son comportement depuis la fonction appelante.

La vision est inversée : dans une chaine de co-routines, la fonction appelante pousse les données vers la fonction appelée. Il est aussi possible de diffuser des données à plusieurs co-routines.

L'application principale des co-routines est de faire de la programmation pseudo-asynchrone tout en gardant une lisibilité proche du code synchrone classique. L'autre avantage est que la co-routine est "maitre" de son état et sait à quel endroit et dans quel état elle peut être interrompue et reprendre son exécution.

Le mot clé ``yield from``, arrivé en Python 3, permet de faire de la *délégation de générateurs*, c'est à dire de créer une sorte de tunnel bidirectionnel entre un générateur et un sous-générateur.

Les slides de la présentation sont disponibles ici : `Générateurs et co-routines <https://github.com/mhugo/pres_coroutines>`_

Merci à tous pour votre présence, on se retrouve au prochain barcamp le 24 mars !