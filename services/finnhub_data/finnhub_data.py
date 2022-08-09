import finnhub
import os
import pandas as pd
import datetime as dt
import time


def finnhub_data(ticker, start, end, delta=1):
    client = finnhub.Client(api_key=os.environ.get('FINNHUB_TOKEN'))

    delta = dt.timedelta(days=delta)

    df = pd.DataFrame(columns=['date', 'headline', 'summary'])
    calls = 0

    while start <= end:
        news = client.company_news(ticker, _from=start.strftime('%Y-%m-%d'), to=(start + delta - dt.timedelta(days=1)).strftime('%Y-%m-%d'))
        calls += 1
        for item in news:
            sub_dict = {'date': [dt.date.fromtimestamp(item['datetime'])], 'headline': [item['headline']], 'summary': [item['summary']]}
            row = pd.DataFrame.from_dict(sub_dict)
            df = pd.concat([df, row], ignore_index=True)
        start += delta
        if calls % 10 == 0:
            print(str(calls) + 'api calls')
            time.sleep(10)

    return df

