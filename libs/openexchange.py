import requests

class OpenExcangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    def latest_json(self):
        return requests.get("{}/latest.json?app_id={}".format(self.BASE_URL, self.app_id)).json()

    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest_json['rates']
        to_rate = rates[to_currency]

        if from_currency == self.latest_json['base']:
            return from_amount * to_rate
        else:
            from_to_usd = from_amount / rates[from_currency]
            return from_to_usd * to_rate