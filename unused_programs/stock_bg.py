#
# Program to read input from .csv files
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

fileName = "../data/meta.csv"
stocks = pd.read_csv(fileName)
stocks_filtered = stocks[stocks['market_cap'] > 1e+12]
print(stocks_filtered)

plt.rcdefaults()
fig, ax = plt.subplots()
#
# # Example data
#
ax.barh(stocks_filtered['ticker'], stocks_filtered['market_cap'], align='center')
ax.set_yticks(stocks_filtered['ticker'], labels=stocks_filtered['name'])
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Dollars in trillions')
ax.set_title('Stocks above a 1 trillion market cap')
#
plt.show()
