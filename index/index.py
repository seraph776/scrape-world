#!/usr/bin/env python3
"""
created: 2022-10-06
@author: seraph1001100
mission: Scrape the hidden paragraph tag on this page
"""
from requests_html import HTMLSession

BASE_URL = 'https://scrape.world/'

session = HTMLSession()
page = session.get(BASE_URL).html

using_find = page.find('div.container', first=True).find('p')[3].text
using_xpath = page.xpath('/html/body/div/div/p[4]', first=True).text


