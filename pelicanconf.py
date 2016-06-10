#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'starofrainnight'
SITENAME = 'StarOfRainNight\'s Home'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
THEME = "bootstrap2-dark"
THEME_BOOTSTRAP2_DARK_HIDE_FONT_AWESOME = True

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("My Chinese Blog", "/cht"),)

# Social widget
SOCIAL = ()

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud", "minify", "pelican_lyx_reader"]

DISQUS_SITENAME = "starofrainnighteng"

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_METADATA = {
    'status': 'draft',
}

TAG_CLOUD_SORTING = 'size'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
