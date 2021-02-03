# imports and dependecies
import os
from os import listdir
import pandas as pd
import datetime

# obtain needed data for processing
# Filter out data to use volatility on data an hour prior to market open
# Market Open: NYSE open Monday-Friday 9:30am to 4pm. Eastern time
def raw_to_data(fp):
    
    # read in data
    data = pd.read_csv(fp)
    # convert time column time zone
    data.time = pd.DatetimeIndex(data.time).tz_localize('US/Eastern')
    # filter out data for use
    market_open_time = datetime.time(hour=9, minute=30)
    market_1hr_early = datetime.time(hour=8, minute=30)
    data = data.loc[data.time.apply(lambda date:(date.time()<=market_open_time)
                        and (date.time()>=market_1hr_early)
                        )]
    data.reset_index(drop=True, inplace=True)
    
    return data