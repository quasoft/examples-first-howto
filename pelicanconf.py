#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Quality Software'
SITENAME = 'How-to Snippets'
SITEURL = 'http://localhost:8000/'
AUTHORURL = 'http://quasoft.net/'
HOMEPAGEBTN = 'Start'

PATH = 'content'

TIMEZONE = 'Europe/Sofia'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = ('%d/%m/%Y')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ['images']
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension',]
#THEME = 'themes/niu-x2'
THEME = 'C:/Projects/examples-first-howto/themes/niu-x2'

THEME_LOC = SITEURL + 'theme'
NIUX2_LIB_FONTAWESOME = THEME_LOC
NIUX2_LIB_JQUERY = THEME_LOC + '/js/jquery.min.js'
