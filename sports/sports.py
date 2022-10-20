#!/usr/bin/env python3
"""
created: 2022-10-06
@author: seraph1001100
project: 
"""
from requests_html import HTMLSession

BASE_URL = 'https://scrape.world'
url = BASE_URL + '/sports'


session = HTMLSession()
page = session.get(url)

sport_links = [lnk.absolute_links for lnk in page.html.find('h4')]

print(sport_links)