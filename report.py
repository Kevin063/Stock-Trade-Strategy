from basic import load_data, back_check

oblist=['W','AMZN','FB']
def compare(strategy1,strategy2,length):
    for symbol in oblist:
        data = load_data(symbol, length)
        print( str(symbol+" "+str(strategy1.__name__)+' prodit= '+str(back_check(strategy1, data, length, 100))+' '+str(strategy2.__name__) + ' prodit= ' + str(back_check(strategy2, data, length, 100))))