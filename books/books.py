#!/usr/bin/env python3
"""
created: 2022-10-08
@author: seraph1001100
mission: Scrape the info for How to Get Filthy Rich
mission: Scrape and download all multimedia
mission: Scrape and monitor the sale price for each book
"""
from requests_html import HTMLSession

BASE_URL = 'https://scrape.world'
url = BASE_URL + '/books'

session = HTMLSession()
page = session.get(url).html


script = """

  $(document).ready(function(){
    $("#button1").click(function(){
      $("#div1").load("static/early.txt");
    });
  });

  $(document).ready(function(){
    $("#button2").click(function(){
      $("#div2").load("static/filthy.txt");
    });
  });

  $(document).ready(function(){
    $("#button3").click(function(){
      $("#div3").load("static/orconomics.txt");
    });
  });

"""

#page.render(sleep=2, script=script)

#filthy = page.find('div.book-filthy')
l = page.absolute_links
#res = page.render(script=script)

print(l)






# -----------------------------------------

# BASE_URL = 'https://scrape.world'
# url = BASE_URL + '/static/filthy.txt'
#
# session = HTMLSession()
# page = session.get(url).html
# page.render()
#
#
# print(page.html)