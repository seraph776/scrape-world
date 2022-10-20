#!/usr/bin/env python3
"""
created: 2022-10-08
@author: seraph1001100
mission: Scrape every Toronto Pine Needles game
"""
import csv

from login.login_authentication import login_session
from login.config import username, password

BASE_URL = 'https://scrape.world'
login_url = BASE_URL + '/login'
url = BASE_URL + '/results'

api_url = BASE_URL + '/results_data'
params = {'_data': '1665277923903'}

session = login_session(username, password, login_url)
response = session.get(api_url, params=params)

json_obj = response.json()
game_data = (json_obj['data'])


def get_team_results(team_name):
    records = []
    result = [game for game in game_data if game['away'] == team_name or game['home'] == team_name]
    for game in result:
        day = game['day']
        home = game['home']
        away = game['away']
        home_score = game['goals_home']
        away_score = game['goals_away']
        extra_time_lose = game['extra_time_loss']
        record = (day, home, home_score, away, away_score, extra_time_lose)
        records.append(record)

    with open('results.csv', 'w', newline='', encoding='utf-8') as file:
        dictWriter = csv.DictWriter(file, fieldnames=['Day', 'Home', 'HomeScore', 'Away', 'AwayScore', 'ExtraLose'])
        dictWriter.writeheader()
        for game in records:
            day, home, home_score, away, away_score, extra_time_lose = game[0], game[1], game[2], game[3], game[4], \
                                                                       game[5]
            dictWriter.writerow(
                {'Day': day, 'Home': home, 'HomeScore': home_score, 'Away': away, 'AwayScore': away_score,
                 'ExtraLose': extra_time_lose})


team = 'Toronto Pine Needles'

get_team_results(team)
