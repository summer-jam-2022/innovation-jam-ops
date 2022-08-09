### Trains Random Forest Classifier on single stock

Runs with command line inputs

Required:
* --ticker (string, ticker of the stock being predicted)

Optional:
* --estimators (int, number of decision trees in random forest)
* --precision (float, target precision of the model)
* --predictors (list of strings)
  * Available Predictors:
  * Close: closing value of a stock for a given day
  * Open: opening value of a stock for a given day
  * High: highest value of a stock for a given day
  * Low: lowest value of a stock on a given day
  * Volume: number of times a stock is traded on a given day
  * Weekly Average: rolling average of the last 7 closing prices
  * Quarterly Average: rolling average of the last 91 closing prices
  * Yearly Average: rolling average of the last 365 closing prices
  * Sentiment*: sentiment of the headlines surrounding a given stock (preferably only used for major companies with sufficient media attention)
  * Weekly Sentiment*: rolling average of the last 7 days of media sentiment surrounding a given stock
* --start_date (datetime, mm/dd/yyyy, start of the prediction)
* --end_date (datetime, mm/dd/yyyy, end of the prediction)
* --pred_days (int, amount of days predicted using the training)
* --samples_split (int, higher minimum sample split for faster performance lower precision)

*Sentiment and Weekly Sentiment both require a Finnhub api key stored as an environment variable named FINNHUB_TOKEN