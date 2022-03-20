import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import datetime
import basic
import strategy
# pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 15)
from basic import *
data=load_data('AMZN',100)
print(cal_profit(strategy.keep(work_date(get_date(100)[0], get_date(100)[1])), data, 100))
