#
# Program to read input from .csv files
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

fileName = "../data/pricedata_reshaped.csv"
data = pd.read_csv(fileName)

dates = [date for date in data['date']]
datetimes = []
for date in dates:
    datetimes.append(dt.strptime(date, '%Y-%m-%d'))

plt.plot(datetimes, data['AAPL'])
plt.show()

#a test to see
