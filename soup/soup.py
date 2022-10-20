#!/usr/bin/env python3
"""
created: 2022-10-06
@author: seraph1001100
mission: Scrape every figure of speech link
"""

from requests_html import HTMLSession


BASE_URL = 'https://scrape.world'
url = BASE_URL + '/soup'

session = HTMLSession()
page = session.get(url).html

figure_of_speech = page.find('ul.figure_of_speech', first=True).links

