### Trains a random forest classifier following a number of parameters

* ticker (ticker of stock being modeled)
* start_date (date of beginning of training data)
* end_date (date of last day of prediction data)
* pred_days (number of days being predicted)
* predictors (set of predictors used in the model)
  * Available Predictors:
  * Close: closing value of a stock for a given day
  * Open: opening value of a stock for a given day
  * High: highest value of a stock for a given day
  * Low: lowest value of a stock on a given day
  * Volume: number of times a stock is traded on a given day
  * Weekly Average: rolling average of the last 7 closing prices
  * Quarterly Average: rolling average of the last 91 closing prices
  * Yearly Average: rolling average of the last 365 closing prices
  * Sentiment: sentiment of the headlines surrounding a given stock (preferably only used for major companies with sufficient media attention)
  * Weekly Sentiment: rolling average of the last 7 days of media sentiment surrounding a given stock
* estimators (number of decision trees used in the Random Forest Classifier)
* samples_split (minimum number of samples required to split a node)
* target_precision (target precision of the model)