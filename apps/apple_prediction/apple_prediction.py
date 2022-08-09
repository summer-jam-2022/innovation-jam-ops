import pandas as pd
import matplotlib.pyplot as plt

import pandas_datareader as web
from datetime import datetime as dt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

# Preprocessing Data

ticker = "AAPL"

start = dt(2010,1,1)
end = dt(2020,1,1)

apple = web.DataReader(ticker, 'yahoo', start, end)

data = apple[['Close']]
data = data.rename(columns={'Close':'Actual_Close'})
data['Target'] = apple.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])['Close']

apple_prev = apple.copy()
apple_prev = apple_prev.shift(1)

predictors = ['Close', 'High', 'Low', 'Open', 'Volume']
data = data.join(apple_prev[predictors]).iloc[1:]

# Model

model = RandomForestClassifier(n_estimators=500, min_samples_split=10, random_state=1)
target_precision = 0.6

train = data.iloc[:-150]
test = data.iloc[-150:]

model.fit(train[predictors], train['Target'])

preds = model.predict_proba(test[predictors])[:, 1]
preds = pd.Series(preds, index=test.index)
preds[preds >= target_precision] = 1
preds[preds < target_precision] = 0

combined = pd.concat({'Target': test['Target'], 'Predictions': preds})

# Chart

plt.plot(preds, color='orange')
plt.plot(test['Target'], color='blue')
plt.show()

print(precision_score(test["Target"], preds))





