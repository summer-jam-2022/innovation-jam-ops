import requests
import pandas as pd
import os


def get_data(tweet):
    data = {'id': [tweet['id_str']], 'created_at': [tweet['created_at']], 'text': [tweet['full_text']]}
    return data


def process_data(query, num_tweets=100, exclude='retweets'):
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
    params = {'q': query,
              'tweet_mode': 'extended',
              'lang': 'en',
              'count': str(num_tweets),
              'exclude': exclude}

    tweets = requests.get(
        'https://api.twitter.com/1.1/search/tweets.json',
        params=params,
        headers={'authorization': 'Bearer ' + BEARER_TOKEN})

    if tweets.status_code == 200:
        df = pd.DataFrame()

        for tweet in tweets.json()['statuses']:
            row = pd.DataFrame.from_dict(get_data(tweet))
            df = pd.concat([df, row], ignore_index=True)

        drop = []
        for i, tweet in enumerate(df['text']):
            while '@' in tweet:
                stem = tweet[:tweet.find('@')]
                post = tweet[tweet.find('@')+1:]
                if post.find(' ') == -1:
                    post = ''
                else:
                    post = post[post.find(' ') + 1:]
                tweet = stem + post

            while 'http' in tweet:
                stem = tweet[:tweet.find('http')]
                post = tweet[tweet.find('http') + 4:]
                if post.find(' ') == -1:
                    post = ''
                else:
                    post = post[post.find(' ') + 1:]
                tweet = stem + post

            while 's:/' in tweet:
                stem = tweet[:tweet.find('s:/')]
                post = tweet[tweet.find('s:/') + 3:]
                if post.find(' ') == -1:
                    post = ''
                else:
                    post = post[post.find(' ') + 1:]
                tweet = stem + post

            if tweet.count('#') > 12:
                drop.append(i)

            df['text'].iloc[i] = tweet

        df = df.drop(drop)
        return df

    else:
        return tweets.status_code


if __name__ == '__main__':
    print(process_data('test'))




