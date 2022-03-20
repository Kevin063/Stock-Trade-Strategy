import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import datetime
def load_data(symbol,length):
    #Symbol:Stock symbol to pull data
    #Length: days of data pulled , until today
    data=yf.download(symbol,
                      end=datetime.date.today().strftime('%Y-%m-%d'),
                      start=(datetime.date.today()- datetime.timedelta(length-1)).strftime('%Y-%m-%d'),
                      progress=False)
    # data=fill_data(data)
    return data
def work_date(start,end):
    data=yf.download('W',
                      end=end,
                      start=start,
                      progress=False)
    return pd.DataFrame(data.index)
def get_date(length):
    return (datetime.date.today()- datetime.timedelta(length-1)).strftime('%Y-%m-%d'),datetime.date.today().strftime('%Y-%m-%d')
def cal_profit(strategy,data,base):
    profit=0
    hold=0
    mut=0
    for index,row in strategy.iterrows():
        if(row['action']==1):
            if(mut==0):
                mut=float(base/data.loc[[row['Date'].strftime('%Y-%m-%d')]]['Open'][0])
                #Calculate the ratio of base and the first share
            profit=profit-data.loc[[row['Date'].strftime('%Y-%m-%d')]]['Open'][0]
        if (row['action'] == -1):
            profit = profit + data.loc[[row['Date'].strftime('%Y-%m-%d')]]['Open'][0]
    return profit*mut