# -*- coding: utf-8 -*-
AUTHOR = u'Python-Nantes'
SITENAME = u"Python-Nantes"
TAGLINE = u"Rencontres pythoniques et ligériennes"
SITEURL = 'http://python-nantes.github.io'

PATH = 'sources/'
OUTPUT_PATH = 'www/'

TIMEZONE = 'Europe/Paris'

PLUGIN_PATH = "pelican-plugins/"
PLUGINS = ['gravatar']

COVER_IMG_URL = '/images/sidebar.jpg'

LINKS = (
    ('AFPY', 'http://www.afpy.org/'),
    ('Python', 'https://www.python.org/'),
    ('La Cantine', 'http://cantine.atlantic2.org/'),
)

SOCIAL = (
    ('twitter', 'https://twitter.com/PythonNantes'),
    ('github', 'https://github.com/python-nantes'),
    ('rss', "/feeds/all.atom.xml")
)

PAGE_DIR = 'pages'

STATIC_PATHS = ['images', 'documents']

#EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DEFAULT_PAGINATION = 5

#GOOGLE_ANALYTICS = 'XXX'

#DISQUS_SITENAME = 'xxx'
