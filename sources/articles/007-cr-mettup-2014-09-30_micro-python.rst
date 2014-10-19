Barcamp & micro-python
##########################################

:date: 2014-10-19
:tags: python,microcontrôleur,nantes,microcontroller
:category: événements
:author: Pierre Aufrere
:email: twildawnight@gmail.com
:summary: Compte-rendu du groupe barcamp sur micro-python.


Pour le barcamp Python du 30 Septembre, nous étions 6 à s'être intéressés à cette mystérieuse carte micro-python. C'est donc convivialement installés autour d'une table qu'on a pu en savoir plus.

Compte rendu.

Présentation
============
Né d'un projet Kick-Starter, micro-python est un microcontrôleur embarquant un interpréteur d'un dialect de Python 3.
Après la réussite du financement sur Kick-Starter, un exemplaire a été envoyé à tous les gens y ayant participé. Puis chaque personne s'étant manifestée sur leur newsletter a pu en avoir un.
Désormais la boutique Internet est ouverte à tous. Si ça vous fait déjà rêver, c'est `par ici <http://micropython.org/>`_.

C'est donc un petit joujou d'open hardware que nous avons pu voir en action. La bestiole est équipée d'un processeur ARM et coûte environ 35€. Pour l'instant on commande depuis le Royaume-Uni, donc c'est en Livres...
Concernant le stockage, deux options. Une mémoire flash de 128Ko et un port pour micro-SD.
Pour le reste, notre micro-copain intègre des accéléromètres. Il y a une démo sur le site pour le transformer en souris. Par contre, pas de gyroscope, donc *exit* la position en temps réelle native. En revanche, il existe de nombreux
shield (modules additionnels) que l'on peut déjà commander et dont le prix est assez bas. On citera un afficheur LCD, un touch-pad et de quoi supporter le wi-fi.
Enfin, la carte présente quatre (4) LEDs. Rouge, jaune, verte et bleue. L'intensité de cette dernière peut être réglée.
La question s'est évidemment posée de l'avantage par rapport à son *concurrent* direct, le Raspberry Pie. Deux arguments principaux sont ressortis. D'abord la consommation électrique bien inférieure de micro-python : l'absence de processeur graphique
est l'une des raisons. Il a également été évoqué les fuites de courant des ports USB du Rasberry Pie. De plus, ces derniers ne peuvent pas être désactivés, donc pas d'optimisation de la consommation possible. Second argument en faveur de
micro-python, éviter *l'over-kill*. En effet, pour la pluspart des utilisations d'un microcontrôleur, un Raspberry Pie fait un peu office de bombe nucléaire.
Petit plus de la carte, elle présente une documentation électrique fournie et claire, écrite en blanc au dos de celle-ci.

Concernant le logiciel, c'est donc un dialecte de Python 3. Cette variante est disponible et compilable sur de nombreuses architectures autres que ARM. Le code source est disponible sur
`GitHub <https://github.com/micropython/micropython>`_. En plus de cela, il existe un `repo <https://github.com/micropython/micropython-lib>`_ de différentes bibliothèques adaptées pour micro-python. On peut notamment y trouver pip.

Let's roll
==========
*C'est bien mignon tout ça, mais qu'en fait-on ?* me direz-vous. Pas d'impatience, voici le moment venu du test !

Que la lumière soit
--------------------
On commence par sortir en boîte :). Notre démonstrateur nous sort sa plus jolie boucle *while* pour éclairer les LEDs en séquences. Vidéo du résultat ci-dessous avec en prime le code source en arrière plan.

.. youtube:: LCrE0T3FtEU
	:width: 500
	:height: 280

Ce test est l'occasion de découvrir comment on code et déploie. Le processeur cherche successivement sur la micro-SD ou sur la flash un fichier **main.py** qui sert de point d'entrée au programme. Lors de l'écriture sur la
mémoire flash, la LED rouge s'allume et s'éteint à la fin de l'opération. Un petit reboot et le tour est joué. Il est possible de faire de l'inlining assembleur pour optimiser les chemins critiques et un portage de l'API C de Python est disponible. De quoi s'occuper donc.

Moteur, ça tourne
-----------------
Seconde démo, utilisation d'un servomoteur. Même logique concernant le code et le déploiement. Concrètement, une classe Servo permet de contrôler le servo :

.. code:: python

	brain = pyb.Servo(1)

On peut ensuite changer l'angle, en degré :

.. code:: python

	brain.angle(45)
	brain.angle(-60)

Consulter l'angle courant :

.. code:: python

	servo1.angle()
	-60

Et aussi changer l'angle en spécifiant un temps de transition, en millisecondes :

.. code:: python

	servo1.angle(50, 1000)

Dans le contexte de ce test, comment ne pas parler des drones ? Du coup, nous avons évoqué une conférence TED sur les
`drones agiles <http://www.ted.com/talks/raffaello_d_andrea_the_astounding_athletic_power_of_quadcopters?language=en>`_
et aussi le projet open-source de drone `Paparazzi <http://wiki.paparazziuav.org/wiki/Main_Page>`_.

Digression
==========
Beaucoup d'effervescence lors de cette rencontre, et donc quelques digressions. Le sujet le plus *complet* était sans doute l'opposition entre pip et gestionnaire de paquets (celui du système lorsque présent) pour la gestion des bibliothèques.

pip permet d'installer des paquets Python sans gestion complexe de dépendance non python (compilateur C/C++). Couplé avec les environnements virtuels, il résout de nombreux problèmes mais reste avant tout une solution de contournement. Cependant, faire sans peut s'avérer difficile.

L'alternative beaucoup plus stable reste donc l'utilisation du gestionnaire de paquet du système. Hors toutes les bibliothèques Python ne sont pas packagées... Donc, si l'on souhaite rester *rigoureux* il faudra sans-doute **repackager** quelques bibliothèques. Il semble que ce soit la stratégie de `Reddit <http://www.reddit.com/>`_.

Les autres projets évoqués :
	* `Association PING <http://www.pingbase.net/>`_
	* `Busybee <http://www.busybee.io/faq/>`_
