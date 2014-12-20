How to install
#################

Installing
=============

Clone the repository and recursively init submodules::

  $ git clone git@github.com:AFPy/python-nantes.git
  $ cd python-nantes
  $ git submodule update --init --recursive

You may want to work in a virtualenv::

  $ virtualenv venv
  $ . venv/bin/activate

Now install pelican::

  $ pip install pelican

Setting up
=============

Make a localsettings::

  $ cp localsettings.py.sample localsettings.py

Change ``SITEURL`` value to eg ``http://localhost:8000``
if you plan to use the dev server (see below).

Change ``OUTPUTPATH`` value to eg. ``www/``.

Using
===========

Remember to first activate your virtualenv, if needed.

Build the blog::

  $ make -e CONFFILE=localsettings.py html

You can preview it by serving it with::

  $ make serve
