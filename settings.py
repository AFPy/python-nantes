# -*- coding: utf-8 -*-
AUTHOR = u'Python-Nantes'
SITENAME = u"Python-Nantes"
TAGLINE = u"Rencontres pythoniques et ligériennes"
SITEURL = 'http://nantes.afpy.org'

PATH = 'sources/'
OUTPUT_PATH = 'www/'

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

TIMEZONE = 'Europe/Paris'

PLUGIN_PATHS = ["pelican-plugins/"]
PLUGINS = ['gravatar']

COVER_IMG_URL = '/images/sidebar.jpg'

#LINKS = (
#    ('AFPY', 'http://www.afpy.org/'),
#    ('Python', 'https://www.python.org/'),
#    ('La Cantine', 'http://cantine.atlantic2.org/'),
#)

SOCIAL = (
    ('envelope', 'http://lists.afpy.org/listinfo/nantes'),
    ('user', 'http://www.meetup.com/Nantes-Python-Meetup/'),
    ('rss', '/feeds/all.atom.xml'),
    ('twitter', 'https://twitter.com/PythonNantes'),
    ('github', 'https://github.com/afpy/python-nantes'),
)

MENUITEMS = (
    ('A propos', '/pages/a-propos-de-python-nantes.html'),
    ('Archives', '/archives.html')
)

STATIC_PATHS = ['images', 'documents', 'extra/CNAME', 'presentations']

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

DEFAULT_PAGINATION = 5

#GOOGLE_ANALYTICS = 'XXX'

#DISQUS_SITENAME = 'xxx'
