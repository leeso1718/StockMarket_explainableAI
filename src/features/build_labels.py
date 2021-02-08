# imports and dependencies
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import datetime
import numpy as np

import os

'''
This function calculates the volatility change before and after the market open.
Then it correspondinglyl creates a label for each day.
The output is a table with two rows: one with image_id (e.g. '2019-01-30.png') and another with label (e.g. '8').
'''


def label(data, market_data, output_fp):
    '''
    data: data with volatility during 1 hour before market open
    market_data: data with volatility during market open
    '''
    # Calculate mean volatility during 1 hour before marekt open each day
    before_vol = data.assign(date=data.time.apply(lambda x: x.date()))
    before_vol = before_vol[['date','Volatility']]
    before_vol_mean = before_vol.groupby('date')['Volatility'].mean()
    before_vol_mean = pd.DataFrame(before_vol_mean)
    before_vol_mean.rename(columns={"Volatility":"Mean Vol Before Open"},inplace=True)
    
    # Calculate mean volatility during marekt open
    after_vol = market_data.assign(date=market_data.time.apply(lambda x:x.date()))
    after_vol = after_vol[['date','Volatility']]
    after_vol_mean = after_vol.groupby('date')['Volatility'].mean()
    after_vol_mean = pd.DataFrame(after_vol_mean)
    after_vol_mean.rename(columns={"Volatility":"Mean Vol After Open"},inplace=True)

    # Calculate the score for each day
    combined = before_vol_mean.merge(after_vol_mean, left_on='date', right_on='date')
    combined['score'] = combined['Mean Vol After Open']/combined['Mean Vol Before Open']
    combined['percentile'] = combined.score.rank(pct = True)
    combined['Percentile Class'] = combined.percentile//0.1
    combined['Percentile Class'] = combined['Percentile Class'].astype(int).astype(str)
    
    # Create a table of image id (date) and the corresponding label
    img_lbl_dir = combined
    img_lbl_dir['image_id'] = img_lbl_dir.index
    img_lbl_dir['image_id'] = img_lbl_dir['image_id'].apply(lambda x: str(x) + ".png")
    img_lbl_dir = img_lbl_dir.reset_index()
    img_lbl_dir['label'] = img_lbl_dir['Percentile Class']
    img_lbl_dir = img_lbl_dir[['image_id', 'label']]
    
    # Save mg_lbl_dir to output_fp
    name = 'image_label_dir.csv'
    path = os.path.join(output_fp, name)
    img_lbl_dir.to_csv(path, index=False)
    
    return 