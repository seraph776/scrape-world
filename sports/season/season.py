#!/usr/bin/env python3
"""
created: 2022-10-06
@author: seraph1001100
mission: Scrape the projected wins for each team
"""
from login.login_authentication import login_session
from login.config import username, password
import csv

BASE_URL = 'https://scrape.world'
login_url = BASE_URL + '/login'
url = BASE_URL + '/season'

session = login_session(username, password, login_url)

page = session.get(url).html

teams = [t.text for t in page.find('td') if t.attrs.get('data-stat') == 'team_name']
wins = [t.text for t in page.find('td') if t.attrs.get('data-stat') == 'wins_avg']

result = list(zip(teams, wins))


with open('results.csv', 'w', newline='') as file:
    dictWriter = csv.writer(file, delimiter=',')
    dictWriter.writerow(['Teams', 'Wins'])
    dictWriter.writerows(result)
