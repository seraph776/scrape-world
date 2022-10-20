#!/usr/bin/env python3
"""
created: 2022-10-13
@author: seraph1001100
project: 
"""
from requests_html import HTMLSession
from login.login_authentication import login_session
from login.config import username, password
import os

BASE_URL = 'https://scrape.world'
login_url = BASE_URL + '/login'
url = BASE_URL + '/books'

session = login_session(username, password, login_url)
page = session.get(url)

pics = [BASE_URL + t.attrs['src'] for t in page.html.find(selector='img')]
media = [BASE_URL + t.attrs['src'] for t in page.html.find(selector='source')]

multimedia_links = pics + media
multimedia_dir = 'multimedia'

if not os.path.exists(multimedia_dir):
    os.mkdir(multimedia_dir)

for link in multimedia_links:
    r = session.get(link)
    filename = link.split('/')[-1]
    with open(os.path.join(multimedia_dir,filename), 'wb') as file:
        for chunk in r.iter_content(chunk_size=128):
            file.write(chunk)
