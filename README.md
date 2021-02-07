# StockMarket_explainableAI
Contributing Members: 
- Sohyun Lee
- Shin Ehara
- Jou-Ying Lee

## Abstract
Deep learning architectures are now publicly recognized and repeatedly proven to be powerful in a wide range of high-level prediction tasks. While these algorithms’ modeling generally have beyond satisfactory performances with apposite tuning, the long-troubling issue of this specific learning lies in the un-explainability of model learning and predicting. This interpretability of “how” machines learn is often times even more important than ensuring machines outputting “correct” predictions. Especially in the field of finance, users’ ability to dissect how and why an algorithm reached a conclusion from a business standpoint is integral for later applications of i.e., to be incorporated for business decision making, etc. This project studies similar prior work done on image recognition in the financial market and takes a step further on explaining predictions outputted by the Convolutional Neural Network by applying the Grad-CAM algorithm. 

## Directory Structure
* **config**</br>
	This folder contains json files for main and testing parameters
	* `data_params.json`</br>contains parameters for running main on all data
	* `test_params.json`</br>contains parameters for running main on test data
* **data**</br>
	This folder contains all stock data from time series to image representation</br>
	
	**TSLA**</br>
	* RawData</br> This folder contains all obtained raw time series data
	* ProcData</br>This folder contains all processed csv files from RawData
	* TestData</br> This folder contains test target
	
	**imgs**</br>
	* all</br> This folder contains all images converted from time series
	* test</br> This folder contains test images converted by main

* **src**
	* *data*
		* `make_dataset.py`</br>scripts to obtain necessary data for this project
	* *features*
		* `build_features.py`</br>scripts to build features from merged data
		* `build_labels.py`</br>scripts to create labels for image classification
		* `build_images.py`</br>scripts to convert and save time series data to images
