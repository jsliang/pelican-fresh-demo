#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'jsliang'
SITENAME = u'Fresh: a responsive Pelican theme that uses HTML5'
SITEURL = 'http://jsliang.com/pelican-fresh-demo/blog'

FEED_DOMAIN = SITEURL

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'pelican-fresh'

DISQUS_SITENAME = "jsliang"

GITHUB_URL = "http://github.com/jsliang/pelican-fresh-demo"

HIDE_CATEGORIES_FROM_MENU = False

MENUITEMS = [('Archives', '%s/archives.html' % SITEURL)]

GOOGLE_ANALYTICS = "UA-37740364-1"
GOOGLE_CUSTOM_SEARCH = "000728178517198415282:4k49jvwgnvy"

