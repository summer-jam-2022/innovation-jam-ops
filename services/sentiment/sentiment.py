from textblob import TextBlob
import pandas

def avg_sentiment(strings):
    total = 0
    for string in strings:
        blob = TextBlob(string)
        total += blob.sentiment.polarity
    if len(strings) != 0:
        return total / len(strings)
    else:
        return -10
