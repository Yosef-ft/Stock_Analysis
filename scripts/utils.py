import pandas as pd
import numpy as np


class DataUtils:
    def load_news_data(self):
        news = pd.read_csv('../data/raw_analyst_ratings.csv/raw_analyst_ratings.csv')

        return news

    def load_historical_data(self, ticker: str):
        ticker_data = {'AAPL' : 'AAPL_historical_data', 'AMZN' : 'AMZN_historical_data',
                       'GOOG' : 'GOOG_historical_data', 'META' : 'META_historical_data',
                       'MSFT' : 'MSFT_historical_data', 'NVDA' : 'NVDA_historical_data',
                       'TSLA' : 'TSLA_historical_data'}
        
        hist_data = pd.read_csv(f'../data/yfinance_data/yfinance_data/{ticker_data[ticker]}.csv')

        return hist_data

