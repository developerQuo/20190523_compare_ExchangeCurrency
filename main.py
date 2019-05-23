#!python
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("content-type: text/html; charset-utf-8\n")

from db_process import create_data
import pandas
# create_data()

  #국가목록생성
country_list = [line.strip() for line in open("data/country_list", 'r', encoding='UTF8')]

def draw_table(select):
    df = pandas.read_csv('data/'+select).sort_values(by=['환율','은행'])
    table = df.to_html(index=False, escape=True, justify='center')

    return table

import cgi
form = cgi.FieldStorage()

def get_country():  #통화선택리스트 가져오기
    listStr = ''
    for item in country_list:
        listStr += '<input type="radio" name="country" id="{name}" value="{name}" onclick="this.form.submit()">{name}  '.format(name=item)
    return listStr


try:    #form["country"].value를 이용해 내용을 다르게 가져오기
    current_coin = form["country"].value
    table = draw_table(current_coin)
except KeyError:
    current_coin = '미국'
    table = draw_table(current_coin)


print('''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>exchange rate by banks</title>
    <style>
    </style>
  </head>
  <body>
    <h1><a href="main.py">은행별 환율비교</a></h1>

    <form>
    <p>
      <h2>통화선택</h2>
      <ul>
        {listStr}
      </ul>
    </p>
    <p>
      <h2>{current_coin} 환율 추이</h2>
      {desc}
    </p>
    <p>
      <h2>은행별 환율</h2>
        {table}
    </p>
    </form>
  </body>
</html>
'''.format(current_coin=current_coin, desc='description', table=table, listStr=get_country()))
