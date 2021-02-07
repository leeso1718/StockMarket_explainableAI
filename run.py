# dependencies & imports

import sys, json, os
import warnings 
import pandas as pd

warnings.filterwarnings("ignore")
sys.path.insert(0, 'src')

from data import make_dataset
from features import build_features, build_images, build_labels

# define main
def main(targets):
    
    # all case
    if ('all' in targets):
        
        # get all params
        with open('config/data_params.json') as fh:
            data_cfg = json.load(fh)
        
        raw_fp = data_cfg['raw_path']
        time_wdw = data_cfg['time_wdw']
        img_fp = data_cfg['output_img_path']
        
        # merged 8:30-9:30 data
        data = make_dataset.merge_data(raw_fp)
        
    # test case: merged already
    if ('test' in targets):
        
        # get test params
        with open('config/test_params.json') as fh:
            data_cfg = json.load(fh)
        
        raw_fp = data_cfg['raw_path']
        test_fn = data_cfg['file_name']
        time_wdw = data_cfg['time_wdw']
        img_fp = data_cfg['output_img_path']
        
        data_file = os.path.join(test_fp, test_fn)
        data = pd.read_csv(test_data_file, parse_dates = ['time'])
        
    # data with volatility
    data = build_features.feature_engineer(data, time_wdw)
    # data for gramian angular field
    data = make_dataset.gaf_df(data)
    # creates images from polar coordinates, saves them to img_fp
    build_images.gramian_img(img_fp, data)
    
    return 

if __name__ == '__main__':
    
    targets = sys.argv[1:]
    main(targets)
