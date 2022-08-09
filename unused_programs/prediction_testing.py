
from services import pred_buy_sell
import pandas as pd
import datetime as dt

monke = pred_buy_sell('AAPL', dt.datetime(2000,6,4), dt.datetime(2018,1,1), 120, estimators=500, target_precision = 0.6)

validity = []
for day in range(len(monke['Predictions'])):
    if monke['Target'][day] == monke['Predictions'][day]:
        validity.append(1)
    else:
        validity.append(0)
t_positive = 0
f_positive = 0
for day in range(len(monke['Predictions'])):
    if monke['Target'][day] == 1 and monke['Predictions'][day] == 1:
        t_positive += 1
    elif monke['Target'][day] == 0 and monke['Predictions'][day] == 1:
        f_positive += 1

precision = t_positive / (t_positive + f_positive)
print(precision)

monke['Validity'] = pd.Series(validity, index=monke.index)

sum = 0
count = 0
for data in monke['Validity']:
    sum += data
    count += 1

print(sum/count)