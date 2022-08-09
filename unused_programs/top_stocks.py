#
# Program to read input from .csv files
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt


def topStocks(fileName, topNum):
    stocks = pd.read_csv(fileName)
    stocks_filtered = stocks.sort_values(by=['market_cap'], ascending=False)
    return stocks_filtered.loc[stocks_filtered.index[0:topNum]]



