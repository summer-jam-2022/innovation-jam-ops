import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as web
from datetime import datetime as dt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

ticker = "NCR"

start = dt(2010,1,1)
end = dt(2020,1,1)

ncr_hist = web.DataReader(ticker, 'yahoo', start, end)

print(ncr_hist.head())

data = ncr_hist[["Close"]]
data = data.rename(columns = {'Close':'Actual_Close'})
data["Target"] = ncr_hist.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])["Close"]

ncr_prev = ncr_hist.copy()
ncr_prev = ncr_prev.shift(1)

predictors = ['Close', 'High', 'Low', 'Open', 'Volume']
data = data.join(ncr_hist[predictors]).iloc[1:]

# Model

model = RandomForestClassifier(n_estimators=100, min_samples_split=200, random_state=1)

train = data.iloc[:-100]
test = data.iloc[-100:]

model.fit(train[predictors], train['Target'])

preds = model.predict(test[predictors])
preds = pd.Series(preds, index=test.index)

combined = pd.concat({'Target': test['Target'], 'Predictions': preds})

plt.plot(combined['Target'])
plt.plot(preds)
plt.show()

start = 1000
step = 750

def backtest(data, model, predictors, start=1000, step=750):
    predictions = []
    for i in range(start, data.shape[0], step):

        train = data.iloc[0:i].copy()
        test = data.iloc[i:(i+step)].copy()

        model.fit(train[predictors], train["Target"])

        preds = model.predict_proba(test[predictors])[:,1]
        preds = pd.Series(preds, index = test.index)
        preds[preds > 0.6] = 1
        preds[preds <= 0.6] = 0

        combined = pd.concat({"Target": test["Target"], "Predictions": preds})

        predictions.append(combined)

    predictions = pd.concat(predictions)
    return predictions

predictions = backtest(data, model, predictors)
predictions["Predictions"].value_counts()

precision_score(predictions["Target"], predictions["Predictions"])

weekly_mean = data.rolling(7).mean()
quarterly_mean = data.rolling(90).mean()
annual_mean = data.rolling(365).mean()

weekly_trend = data.shift(1).rolling(7).mean()["Target"]

full_predictors = predictors + ["weekly_mean", "quarterly_mean", "annual_mean"]
predictions = backtest(data.iloc[365:], model, predictors)

precision_score(predictions["Target"], predictions["Predictions"])

predictions["Predictions"].value_counts()


