# StockMarket_explainableAI
Contributing Members: 
- Sohyun Lee
- Shin Ehara
- Jou-Ying Lee

## Abstract
Deep learning architectures are now publicly recognized and repeatedly proven to be powerful in a wide range of high-level prediction tasks. While these algorithms’ modeling generally have beyond satisfactory performances with apposite tuning, the long-troubling issue of this specific learning lies in the un-explainability of model learning and predicting. This interpretability of “how” machines learn is often times even more important than ensuring machines outputting “correct” predictions. Especially in the field of finance, users’ ability to dissect how and why an algorithm reached a conclusion from a business standpoint is integral for later applications of i.e., to be incorporated for business decision making, etc. This project studies similar prior work done on image recognition in the financial market and takes a step further on explaining predictions outputted by the Convolutional Neural Network by applying the Grad-CAM algorithm. 

## Directory Structure
* **config**
	This folder contains json files for main and testing parameters
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
		* `build_images.py`</br>scripts to convert and save time series data to images
