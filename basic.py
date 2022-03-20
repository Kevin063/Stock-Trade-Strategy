import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import datetime

from calculation import round_decimals_up

display_trade=0
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
    cost=0
    maxcost=0
    mut=0
    for index,row in strategy.iterrows():
        #Iterate daily strategy
        if(row['action']==1):
            if(hold!=0):
                continue
                #Calculate the ratio of base and the first share
            profit=profit - get_price(row['Date'],data)#add money adjustment to balance
            hold=hold+1
            cost=cost+data.loc[[row['Date'].strftime('%Y-%m-%d')]]['Open'][0]
            maxcost=refresh(cost,maxcost)#Refresh max usage
            if(display_trade==1):#Show trades in console
                print("Buy at "+str(data.loc[[row['Date'].strftime('%Y-%m-%d')]]['Open'][0])+" On "+row['Date'].strftime('%Y-%m-%d'))
        if (row['action'] == -1):
            if (hold == 0):
                continue
            profit = profit + get_price(row['Date'],data)#add money adjustment to balance
            profit = profit - trading_fee(get_price(row['Date'],data))
            hold=hold-1
            cost=cost-data.loc[[row['Date'].strftime('%Y-%m-%d')]]['Open'][0]#Refresh max usage
            if(display_trade==1):#Show trades in console
                print("Sell at "+str(data.loc[[row['Date'].strftime('%Y-%m-%d')]]['Open'][0])+" On "+row['Date'].strftime('%Y-%m-%d'))
    if(hold==1):
        profit=profit+data.tail(1)['Open'][0]
        profit=profit-trading_fee(data.tail(1)['Open'][0])
    mut=float(base/maxcost)
    return profit*mut
def back_check(strategy,data,length,base):
    return cal_profit(strategy(work_date(get_date(length)[0], get_date(length)[1]),data), data, base)
def get_price(date,data):
    return data.loc[date.strftime('%Y-%m-%d')]['Open']
def refresh(cost,max):
    #Use to refresh max investment put into the stock
    if(cost>max):
        max=cost
    return max
def trading_fee(price,share=1):
    return round_decimals_up(price*5.1/1000000)+round_decimals_up(0.00013*share)
