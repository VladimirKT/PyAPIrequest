'''This app is used to send request to API and get data

'''
from libs.openexchange import OpenExcangeClient

APP_ID = "6dc2501fe6e143d8a53ff77b569a0c3e"

usd_amount = 1000
client = OpenExcangeClient(APP_ID)

gbp_amount = client.convert(usd_amount, 'USD', 'GBP')

print("{} USD is {:2f} GBP".format(usd_amount, gbp_amount))
