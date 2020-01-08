'''***app_api.py is command line app developed by Vladimir Kocis Tubic in Python programming language
   Main purpose is training in web scraping field
HOW TO USE:
    This app is used to send HTTP request to API and get JSON data
    In libs directory was created two modules: 
    -get_app_id.py is used to get app_id by manipulating with webpages via selenium and webdriver
    -openexchange.py is used to send HTTP request (via requests) and to get JSON data
    Eventually, app_api.py parses and calculate data and give us expected result
'''
import time
from libs.openexchange import OpenExchangeClient
from libs.get_app_id import OpenExchangeId

open_excange_id = OpenExchangeId()

APP_ID = open_excange_id.get_app_id()

start = time.time()
client = OpenExchangeClient(APP_ID)

rates = client.latest_json['rates']
end = time.time()
print(end-start)

line_capacity = 0
one_line_list = []
print('\n'+'*' * 51 + ' LIST OF AVAILABLE CURRENCY ' + '*' * 51 + '\n')
for count,key in enumerate(rates, start=1):
    if line_capacity == 12:
        print('  '.join(one_line_list))
        print('\n')
        line_capacity = 0
        one_line_list = []
    elif count == len(rates) and line_capacity != 12:
        one_line_list.append('** {} **'.format(key))
        print('  '.join(one_line_list))
    one_line_list.append('** {} **'.format(key))
    line_capacity += 1

from_currency = input('\n'+'**** Choose from currency: ')
to_currency = input('\n'+'**** Choose to currency: ')
amount = input('\n'+'**** Choose amount: ')

new_amount = client.convert(int(amount), from_currency.upper(), to_currency.upper())

print("\n"+"**** {} {} is {:2f} {}".format(amount, from_currency.upper(),  new_amount, to_currency.upper()))
