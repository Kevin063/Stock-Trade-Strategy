# 1=Buy 0=Hold -1=Sell
from basic import get_price


def initialize_strategy(date):
    date['action']=0
    return date
def hold(date,data):
    st=initialize_strategy(date)
    st.loc[0,'action']=1
    st.loc[len(st)-1,'action']=-1
    return st
def timid(date,data):
    #Sell when raise,buy when drop
    st = initialize_strategy(date)
    for (index, row), numindex in zip(date.iterrows(), range(len(date.index))):
        if (numindex==0):
            continue
        yesterday=get_price(date.iloc[numindex-1][0],data)
        today=get_price(date.iloc[numindex][0],data)
        if(float(today/yesterday)>1.03):
            st.loc[numindex,'action']=-1
        if (float(today / yesterday) < 0.97):
            st.loc[numindex, 'action'] = 1
    return st
def greedy(date,data):
    #Buy when raise,sell when drop
    st = initialize_strategy(date)
    for (index, row), numindex in zip(date.iterrows(), range(len(date.index))):
        if (numindex==0):
            continue
        yesterday=get_price(date.iloc[numindex-1][0],data)
        today=get_price(date.iloc[numindex][0],data)
        if(float(today/yesterday)>1.03):
            st.loc[numindex,'action']=1
        if (float(today / yesterday) < 0.97):
            st.loc[numindex, 'action'] = -1
    return st