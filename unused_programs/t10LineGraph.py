
import top_stocks
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

fileName = "../data/pricedata_reshaped.csv"
data = pd.read_csv(fileName)
topX = 10

dates = [date for date in data['date']]
datetimes = []
for date in dates:
    datetimes.append(dt.strptime(date, '%Y-%m-%d'))

filteredStocks = top_stocks.topStocks("../data/meta.csv", topX)
for i in range(len(filteredStocks)):
    plt.plot(datetimes, data[filteredStocks['ticker'][filteredStocks.index[i]]], label = filteredStocks['ticker'][filteredStocks.index[i]])

plt.legend(loc="upper left")

plt.show()
