#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '@tegarimansyah'
SITENAME = 'Tegar & Words'
SITESUBTITLE = 'Technology, Lifestyle, Idea. Simply Written'
SITE_DESCRIPTION = 'Technology, Lifestyle, Idea. Simply Written from Tegar for you.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Custom Header

HOME_COVER = "assets/images/home.jpg"

HEADER_COVERS_BY_TAG = {
    'cupcake': 'assets/images/rainbow_cupcake_cover.png', 
    'general':"assets/images/article_cover.jpg"
}

AUTHORS_BIO = {
  "tegarimansyah": {
    "name": "Tegar Imansyah",
    "cover": "assets/images/japan-lake.jpeg",
    "image": "assets/images/avatar.jpeg",
    "website": "https://tegarimansyah.github.io",
    "linkedin": "tegarimansyah",
    "github": "tegarimansyah",
    "location": "Indonesia",
    "bio": 'Tegar interested in engineering topics such as Linux, Programming Language, and Embedded System (IoT). Gave some talks in local meet-up and international conference about technology.<br /> Any discussions are welcome. <a href="/pages/about" style="color: #3ea9dd;">>>More about me here <<</a>'
  }
}

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
THEME = 'attila'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['assets']

### Theme specific settings
COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/myblog.css']

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets',
  'pelican_alias'
]