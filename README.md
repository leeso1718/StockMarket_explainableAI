# StockMarket_explainableAI
Contributing Members: 
- Sohyun Lee
- Shin Ehara
- Jou-Ying Lee

## Abstract
blank for now

## Directory Structure
* **data**
	* `merge_filter_data.csv`</br>contains merged processed data of time intervals (8:30AM - 9:30AM EST)
	* `feat_eng_data.csv`</br>contains feature engineered data with volatility column
	* `data_vol.csv`</br>contains date and volatility column

* **src**
	* *data*
		* `make_dataset.py`</br>scripts to obtain necessary data for this project
	* *features*
		* `build_features.py`</br>scripts to build features from merged data
		* `build_labels.py`</br>scripts to create labels for image classification
