# StockMarket_explainableAI
Contributing Members: 
- Sohyun Lee
- Shin Ehara
- Jou-Ying Lee

## Abstract
Deep learning architectures are now publicly recognized and repeatedly proven to be powerful in a wide range of high-level prediction tasks. While these algorithms’ modeling generally have beyond satisfactory performances with apposite tuning, the long-troubling issue of this specific learning lies in the un-explainability of model learning and predicting. This interpretability of “how” machines learn is often times even more important than ensuring machines outputting “correct” predictions. Especially in the field of finance, users’ ability to dissect how and why an algorithm reached a conclusion from a business standpoint is integral for later applications of i.e., to be incorporated for business decision making, etc. This project studies similar prior work done on image recognition in the financial market and takes a step further on explaining predictions outputted by the Convolutional Neural Network by applying the Grad-CAM algorithm. 

Project Website at: https://connielee99.github.io/Explainable-AI-in-Finance/

## Instructions on `python run.py test`
* This project aims to apply the Grad-CAM technique to a CNN model trained on images that represent the volatility record of Tesla Inc.'s stock `(ticker = TSLA)` during the hour prior to the market open every day to predict the stock's volatility during the market hours. For this mid-quarter checkpoint, our `run.py test` generates those images that will be used to train a CNN model, from a raw financial transaction record stored as time series data.
* When you execute this code in the directory, it performs the following things:
	* **Input Data**
		* `test` target works on the data of only 1 day out of all the data we have for 2 years in total. Specifically, it uses the intra-day transaction record from January 15th, 2021.
		* Data are stored as 2 separate files.
			* The first file is at `../data/TSLA/TestData/test_20210115.csv` and covers the transaction data during the hour prior to the market open on that date.
			* The second file is at `../data/TSLA/TestData/test_market_vol_20210115.csv` and covers the transaction data during the market hours on that data. This second data file includes preprocessed data of volatility for the sake of ease for this `test` execution.
	* **Output**
		* The execution results in 2 outputs: an image and a table.
			* **Image**
				* This image is a representation of all the volatility data during the hour prior to the market open on that date, generated using the technique Gramian Angular Field. The image will be stored in the `.png` format.
			* **Table of Label**
				* This table has two columns. One with image IDs and the other with corresponding label to that image. The table will be stored in the `.csv` format.
		* Both the image and table will be stored in `../data/imgs/test`.

## Directory Structure
* **config**</br>
	This folder contains json files for main and testing parameters
	* `data_params.json`</br>contains parameters for running main on all data
	* `test_params.json`</br>contains parameters for running main on test data
* **data**</br>
	This folder contains all stock data from time series to image representation</br>
	**imgs**</br>
	* This folder contains all images converted from time series. ex) 2017-01-02.png
	
	**raw data**</br>
	* `raw_NIFTY100.csv`</br>contains raw stoack market data (time series data)
	
	* `first_combined.csv`</br>contains data after preprocessing (extracting first hour after market open. (9:15-10:15))
	* `gramian_df.csv`
	* `label_dir_2.csv`
* **gradcam_submodule @ fd10ff7**</br>
	This folder is the submodule for gradcam
	
* **notebooks**</br>
	This folder is the notebook directory
	
	* `CNN + Grad-CAM.ipynb`</br>is the development notebook for CNN and GradCam implementation
	* `Data Processing.ipynb`</br>is the notebook that wraps together data cleaning to feature engineering
	* `EDA.ipynb`</br>is the notebook with eda work demonstration
	* `Image Conversion.ipynb`</br>is the notebook with image conversion work done
* **references**</br>
	This folder contains additional information/references in regards to our project
	
	**report_img**</br>
	* This folder contains images extracted from coded notebooks and included in the written report
	* 
* **src**</br>
	This folder contains library codes extracted from notebooks
	
	**features**</br>
	* `build_features.py`</br>scripts to build features from merged data
	* `build_labels.py`</br>scripts to create labels for image classification
	* `build_images.py`</br>scripts to convert and save time series data to images
	**model**</br>
	* `gradcam.py`</br>scripts to implement gradcam

* **test**</br>
      This folder contains test results and test images
      		
* **`Dockerfile`**</br>
	This is the dockerfile necessary to build the environment for this project development
* **`run.py`**</br>
	This is the main python file to execute our program
