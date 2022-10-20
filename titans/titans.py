#!/usr/bin/env python3
"""
created: 2022-10-06
@author: seraph1001100
mission: Scrape the names of the twelve Titans
"""

from requests_html import HTMLSession


BASE_URL = 'https://scrape.world'
url = BASE_URL + '/titans'

session = HTMLSession()
page = session.get(url).html
all_titans = [titan.text for titan in page.find('b')][1:]
print(all_titans)
print(len(all_titans))

