#!/usr/bin/env python3
"""
created: 2022-10-06
@author: seraph1001100
mission: Scrape the total spend for each team
"""
import csv

from login.login_authentication import login_session
from login.config import username, password

BASE_URL = 'https://scrape.world'
login_url = BASE_URL + '/login'
url = BASE_URL + '/spend'

# Login session
session = login_session(username, password, login_url)
page = session.get(url).html

headers = [tag.text for tag in page.find('thead', first=True).find('th')]
table_body = page.find('tbody', first=True).find('tr')


def clean_money(s):
    """Helper function to formate currency strings"""
    return int(s.split(' ')[0].replace('$', '').replace(',', ''))


records = []
for col in table_body:
    team = col.find('td')[0].text
    forwards = clean_money(col.find('td')[1].text)
    defense = clean_money(col.find('td')[2].text)
    goalies = clean_money(col.find('td')[3].text)
    injuries = clean_money(col.find('td')[4].text)
    cap_hit = clean_money(col.find('td')[5].text.split(' ')[0])

    print(f'{team.title()} - ${cap_hit:,}')

    row = {'Team': team,
           'Forwards': forwards,
           'Defense': defense,
           'Goalies': goalies,
           'Injuries': injuries,
           'Cap Hit': cap_hit}

    records.append(row)


with open('projected-spend.csv', 'w', newline='', encoding='utf8') as file:
    dictWriter = csv.DictWriter(file, fieldnames=headers)
    dictWriter.writeheader()
    for row in records:
        dictWriter.writerow(row)
