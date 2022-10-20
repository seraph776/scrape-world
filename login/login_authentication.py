#!/usr/bin/env python3
"""
created: 2022-10-06
@author: seraph1001100
metadoc: This function logins into Scrape World and maintains a persistent session
"""


from requests_html import HTMLSession


def login_session(username: str, password:str, login_url:str) -> HTMLSession:
    """

    :param username: username to log into site
    :param password: password to log into site
    :param login_url: the url the credentials will be posted to
    :return: persistent HTMLSession
    """
    with HTMLSession() as session:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
        login_data = {
            'username': username,
            'password': password,
            'csrf_token': ''
        }

        page = session.get(login_url).html
        token = page.find('input#csrf_token', first=True).attrs['value']
        login_data['csrf_token'] = token

        # Login
        session.post(login_url, data=login_data, headers=headers)
        return session


