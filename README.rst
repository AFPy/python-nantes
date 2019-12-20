Le blog de la communauté Python-Nantes, propulsé par `Pelican <http://docs.getpelican.com/>`_.

* `Blog <http://nantes.afpy.org>`_
* `Repos Github <https://github.com/AFPy/python-nantes>`_


Écrire un article
##################

* Il suffit de le rédiger dans un fichier ``sources/00X-article.rst`` en suivant les exemples existants (metadata).
* L'ajout du fichier dans le repos sur la branche master relancera automatiquement le déploiement du blog en statique.


Générer le blog en local
#########################

* Forker/Cloner le dépôt
* initialiser et mettre à jour les submodules git
* Adapter un fichier de settings ``localsettings.py`` à partir de ``localsettings.py.sample``
* Lancer la génération du blog en local : ``pelican -s localsettings.py``


Framapad
#########

Le framapad suivant est diponible pour toute remarque ou idée
concernant les futurs meetups, le blog, ou autre: `le pad
<https://annuel.framapad.org/p/organisation_meetup_python_nantes>`_
