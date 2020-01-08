'''HOW TO USE:
        This module provides app_id from your https://openexchangerates.org account
   PREREQUISITE:
        With credentials for your account that are entered on input request you get app_id that provides data access.
'''
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver # have to be installed 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from cachetools import cached, TTLCache


class OpenExchangeId:
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def get_app_id(self):

        log_in_mail, log_in_pass = self.enter_account_credentials()

        chrome_options = Options()
        chrome_options.add_argument("--headless") # web browser without GUI

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://openexchangerates.org/account/app-ids")

        # log_in_mail = 'vladimir.kocis.tubic@gmail.com'
        # log_in_pass = 'vladimirapi3101'
       
        email_in = driver.find_element_by_name('email')
        email_in.send_keys(log_in_mail)
        time.sleep(2)

        pass_in = driver.find_element_by_name('pwd')
        pass_in.send_keys(log_in_pass)

        time.sleep(1)

        keys = Keys() 
        pass_in.send_keys(keys.RETURN) 
        time.sleep(1)

        data = driver.page_source

        soup = BeautifulSoup(data, 'html.parser')

        locator = 'input#app-id-126408'
        app_id = soup.select_one(locator).attrs['value']

        return app_id

    def enter_account_credentials(self):
        print('\n'+'***** PLEASE ENTER YOUR https://openexchangerates.org ACCOUNT CREDENTIALS *****')
        e_mail = input('\n'+ '***** email: ')
        password = input('\n'+ '***** password: ')
        return e_mail, password


if __name__ == '__main__':
    openid = OpenExchangeId()
    print(openid.get_app_id())
