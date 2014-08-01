# -*- coding: utf-8 -*-
AUTHOR = u'Python-Nantes'
SITENAME = u"Python-Nantes: rencontres nantaises autour de Python"
SITEURL = 'http://dev.python-nantes.github.io'

PATH = 'sources/'
OUTPUT_PATH = '/var/www/dev.python-nantes.github.io/'

THEME = "pelican-sober"

TIMEZONE = 'Europe/Paris'

LINKS = (
    ('AFPY', 'http://www.afpy.org/'),
    ('Python', 'https://www.python.org/'),
    ('La Cantine', 'http://cantine.atlantic2.org/'),
)

SOCIAL = (
    ('twitter', 'https://twitter.com/PythonNantes'),
    ('github', 'https://github.com/python-nantes')
)

PAGE_DIR = 'pages'

STATIC_PATHS = ['images', 'documents']

#EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DEFAULT_PAGINATION = 5

#GOOGLE_ANALYTICS = 'XXX'

#DISQUS_SITENAME = 'xxx'
