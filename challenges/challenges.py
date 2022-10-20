#!/usr/bin/env python3
"""
created: 2022-10-06
@author: seraph1001100
mission: Scrape every challenge link
"""

from requests_html import HTMLSession


BASE_URL = 'https://scrape.world'
url = BASE_URL + '/challenges'

session = HTMLSession()
page = session.get(url).html

link_list = page.find('ol', first=True)

challenges = [BASE_URL + link.text for link in page.find('ol', first=True).find('h4')]
print(challenges)