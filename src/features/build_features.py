'''
This function builds the Volatility column for modeling
'''
def feature_engineer(data, time_wdw):
    
    # for time series indexing
    data.set_index('time', inplace=True)
    
    # High-Low within minute bar
    data['diff'] = data.high-data.low
    # Volitility Analysis
    vol = data['diff'].rolling(time_wdw).mean()
    data = data.assign(Volatility=vol)
    # for modelling purpose
    data.dropna(axis=0, inplace=True)
    data.reset_index(inplace = True)
    
    return data