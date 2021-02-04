# imports and dependecies
import os
from os import listdir
import pandas as pd
import datetime

'''
This function filters out data to use volatility on data an hour prior to market open
Market Open: NYSE open Monday-Friday 9:30am to 4pm. Eastern time
@ return: pandas dataframe
'''
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

'''
This function merges processed files from raw path to data path
@ return: pandas dataframe
'''
def merge_data(raw_path):
    
    # output dataframe
    output = pd.DataFrame()
    # all files to be processed
    raw_files = listdir(raw_path)
    
    for curr_file in raw_files:
        fp = raw_path + curr_file
        data = raw_to_data(fp)
        output = pd.concat([output, data])
    
    return output