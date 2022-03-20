import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import datetime
import basic
import strategy
# pd.set_option('display.max_columns', 15)
from report import compare

pd.set_option('display.max_rows', 100)
from basic import *
data=load_data('AMZN',100)
compare(strategy.timid, strategy.greedy, 100)
