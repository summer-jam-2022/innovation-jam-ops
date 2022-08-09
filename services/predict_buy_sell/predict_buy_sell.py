import pandas as pd
import pandas_datareader
from datetime import datetime as dt
from sklearn.ensemble import RandomForestClassifier
from finnhub_data import finnhub_data
from sentiment import avg_sentiment


def pred_buy_sell(ticker, start_date=dt(2000,1,1), end_date=dt(2020,1,1), pred_days=30, predictors=['Close', 'High', 'Low', 'Open', 'Volume'],
                  estimators=100, samples_split=10, target_precision=0.5):

    # Preprocessing Data

    stock_info = pandas_datareader.DataReader(ticker, 'yahoo', start_date, end_date)

    data = stock_info[['Close']]
    data = data.rename(columns={'Close': 'True_Close'})
    data['Target'] = stock_info['Close'].rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])

    # Processing extra predictors

    cut_off = 1

    if 'Weekly Average' in predictors:
        stock_info['Weekly Average'] = stock_info['Close'].rolling(7).mean()

    if 'Quarterly Average' in predictors:
        stock_info['Quarterly Average'] = stock_info['Close'].rolling(91).mean()

    if 'Yearly Average' in predictors:
        stock_info['Yearly Average'] = stock_info['Close'].rolling(365).mean()

    if 'Yearly Average' in predictors:
        cut_off = 365
    elif 'Quarterly Average' in predictors:
        cut_off = 91
    elif 'Weekly Average' in predictors or 'Weekly Sentiment' in predictors:
        cut_off = 7
        
    if 'S&P500' in predictors:
        stock_info['S&P500'] = pandas_datareader.DataReader('^GSPC', 'yahoo', start_date, end_date)['Close']

    if 'Sentiment' in predictors or 'Weekly Sentiment' in predictors:
        stock_info['Sentiment'] = ''
        news = finnhub_data(ticker, start_date, end_date, 3)

        for date in stock_info.index:
            daily = news.copy().loc[news['date'] == date.date()]
            if daily.empty:
                stock_info.loc[date, 'Sentiment'] = 0.1
            else:
                stock_info.loc[date, 'Sentiment'] = avg_sentiment(daily['headline'].tolist())

    if 'Weekly Sentiment' in predictors:
        stock_info['Weekly Sentiment'] = stock_info['Sentiment'].rolling(7).mean()

    stock_prev = stock_info.copy()
    stock_prev = stock_prev.shift(1)

    data = data.join(stock_prev[predictors]).iloc[cut_off:]

    # Model

    model = RandomForestClassifier(n_estimators=estimators, min_samples_split=samples_split, random_state=1)

    train = data.iloc[:-pred_days]
    test = data.iloc[-pred_days:]

    model.fit(train[predictors], train['Target'])

    preds = (model.predict_proba(test[predictors]))[:, 1]
    preds = pd.Series(preds, index=test.index)
    preds[preds >= target_precision] = 1
    preds[preds < target_precision] = 0

    combined = pd.concat({'Target': test['Target'], 'Predictions': preds}, axis=1)

    return combined


if __name__ == '__main__':
    print(pred_buy_sell('NCR', start_date=dt(2021,1,1), end_date=dt(2022,8,1), pred_days=30, predictors=['Close', 'High', 'Low', 'Open', 'Volume'],
                  estimators=100, samples_split=10, target_precision=0.5).head())
