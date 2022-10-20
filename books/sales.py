#!/usr/bin/env python3
"""
created: 2022-10-13
@author: seraph1001100
project: 
"""
import csv
import datetime
import time

from login.login_authentication import login_session
from login.config import username, password

BASE_URL = 'https://scrape.world'
URL = BASE_URL + '/books'

LOGIN_URL = BASE_URL + '/login'
SESSION = login_session(username, password, LOGIN_URL)

b = ['early', 'filthy', 'orconimics']


def get_book_price(session, url, param):
    page = session.get(url)

    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    title = (page.html.find(selector=f'.book-{param}', first=True)).find(selector='h4', first=True).text
    price = (page.html.find(selector=f'.book-{param}', first=True)).find(selector='p', first=True).text.lstrip(
        '$').rstrip('CAD')
    record = (title, price, today)
    return record


def save_file(file, data):
    with open(f'{file}.csv', 'a', newline='') as fo:
        writer = csv.writer(fo, delimiter=',')
        writer.writerow(data)


def get_old_price(file):
    with open(f'{file}.csv') as file:
        price = float([i.strip() for i in file][-1].split(',')[1])
    return price


def evaluate_price(session, url, book_param):
    record = get_book_price(session, url, book_param)
    current_price = float(record[1])
    old_price = get_old_price(book_param)

    if current_price < old_price:
        print(f'Buy {record[0]} @ ${current_price}! (previous price: ${old_price})\n>> Emailing alert!')
    else:
        print('Waiting for a better price...')

    save_file(book_param, record)


# while True:
for n in range(20):
    evaluate_price(SESSION, URL, 'early')
    time.sleep(20)
