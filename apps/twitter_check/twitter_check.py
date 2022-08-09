from twitter_data import process_data
import argparse
import pandas as pd
from textblob import TextBlob
import os

parser = argparse.ArgumentParser()
parser.add_argument('--query', '-q', type=str, required=True)
parser.add_argument('--num', '-n', type=int, required=False)

args = parser.parse_args()

if os.environ.get('BEARER_TOKEN') is None:
    print('No bearer token found in environment variables')
    exit()

if args.num:
    tweets = process_data(args.query, num_tweets=args.num)
else:
    tweets = process_data(args.query)

if type(tweets) != pd.DataFrame:
    print('Request error ' + str(tweets))
    exit()

if len(tweets['text']) == 0:
    print('No tweets found')
    exit()

total_sentiment = 0
for tweet in tweets['text']:
    blob = TextBlob(tweet)
    total_sentiment += blob.sentiment.polarity

avg_sentiment = total_sentiment / len(tweets['text'])
print('Average sentiment surrounding "' + args.query + '" is ' + str(avg_sentiment))
