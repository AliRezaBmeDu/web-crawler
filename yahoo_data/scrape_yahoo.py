# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 22:45:28 2024

@author: Reza
"""

import re
from io import StringIO
from datetime import datetime, timedelta

import requests
import pandas as pd


class YahooFinanceHistory:
    timeout = 2
    crumb_link = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
    crumble_regex = r'CrumbStore":{"crumb":"(.*?)"}'
    quote_link = 'https://query1.finance.yahoo.com/v7/finance/download/{quote}?period1={dfrom}&period2={dto}&interval=1d&events=history&crumb={crumb}'

    def __init__(self, symbol, days_back=7):
        self.symbol = symbol
        self.session = requests.Session()
        self.dt = timedelta(days=days_back)

    def get_crumb(self):
        
        # Log the request URL
        print("Request URL:", self.crumb_link.format(self.symbol))
        response = self.session.get(self.crumb_link.format(self.symbol), timeout=self.timeout)
        response.raise_for_status()
        
        # Log request and response details
        print("Request URL:", response.request.url)
        print("Request Headers:")
        for header, value in response.request.headers.items():
            print(f"{header}: {value}")
        print("\nResponse Status Code:", response.status_code)
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        print("\nResponse Content:", response.text)
        
        match = re.search(self.crumble_regex, response.text)
        if not match:
            raise ValueError('Could not get crumb from Yahoo Finance')
        else:
            self.crumb = match.group(1)

    def get_quote(self):
        if not hasattr(self, 'crumb') or len(self.session.cookies) == 0:
            self.get_crumb()
        now = datetime.utcnow()
        dateto = int(now.timestamp())
        datefrom = int((now - self.dt).timestamp())
        url = self.quote_link.format(quote=self.symbol, dfrom=datefrom, dto=dateto, crumb=self.crumb)
        response = self.session.get(url)
        response.raise_for_status()
        
        # Log request and response details
        print("Request URL:", response.request.url)
        print("Request Headers:")
        for header, value in response.request.headers.items():
            print(f"{header}: {value}")
        print("\nResponse Status Code:", response.status_code)
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        print("\nResponse Content:", response.text)
        
        return pd.read_csv(StringIO(response.text), parse_dates=['Date'])


df = YahooFinanceHistory('AAPL', days_back=30).get_quote()








