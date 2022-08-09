import pandas as pd
import matplotlib.pyplot as plt

import pandas_datareader as web
from datetime import datetime as dt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

# Preprocessing Data

start_date = dt(2010,1,1)
end_date = dt(2020,1,1)

stock = web.DataReader('AAPL', 'yahoo', start_date, end_date)

predictors=['Close', 'High', 'Low', 'Open', 'Volume', 'S&P500']

data = stock[['Close']]
data = data.rename(columns={'Close': 'Actual Close'})
data['Target'] = stock.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])['Close']

# Processing extra predictors

cut_off = 1

if 'Weekly Average' in predictors:
    stock['Weekly Average'] = stock['Close'].rolling(7).mean()

if 'Quarterly Average' in predictors:
    stock['Quarterly Average'] = stock['Close'].rolling(91).mean()

if 'Yearly Average' in predictors:
    stock['Yearly Average'] = stock['Close'].rolling(365).mean()

if 'Yearly Average' in predictors:
    cut_off = 365
elif 'Quarterly Average' in predictors:
    cut_off = 91
elif 'Weekly Average' in predictors:
    cut_off = 7

if 'S&P500' in predictors:
    stock['S&P500'] = web.DataReader('^GSPC', 'yahoo', start_date, end_date)['Close']

print(stock.head())

stock_prev = stock.copy()
stock_prev = stock_prev.shift(1)

#data = data.join(stock_prev[predictors]).iloc[cut_off:]

