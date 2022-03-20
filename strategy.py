# 1=Buy 0=Hold -1=Sell



def initialize_strategy(date):
    date['action']=0
    return date
def keep(date):
    st=initialize_strategy(date)
    st.loc[0,'action']=1
    st.loc[len(st)-1,'action']=-1
    return st