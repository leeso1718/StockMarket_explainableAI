# StockMarket_explainableAI
Contributing Members: 
- Sohyun Lee
- Shin Ehara
- Jou-Ying Lee

## Abstract
blank for now

## Directory Structure
-- Data </br>
	- `merge_filter_data.csv`: contains merged processed data of time intervals (8:30AM - 9:30AM EST)</br>
	- `feat_eng_data.csv`: contains feature engineered data with volatility column</br>
	- `data_vol.csv`: contains date and volatility column</br>


```
├── Docker File        <- Makefile with commands like `make data` or `make train`
├── data
│   ├── external       <- Data obtained from third party sources.
│   ├── interim        <- Intermediate time series data that has been transformed and feature engineered.
│   │   └── 


│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```