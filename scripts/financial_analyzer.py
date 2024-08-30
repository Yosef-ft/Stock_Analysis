import talib as ta
import pandas as pd
import matplotlib.pyplot as plt


class TechnicalIndicator:
    def __init__(self, data):
        self.data = data

    def lagging_indicators(self):
        '''
        Lagging indicators are used to confirm trends and often follow the price movement. 
        '''
        self.data['EMA'] = ta.EMA(self.data['Close'], timeperiod=30)
        self.data['WMA'] = ta.WMA(self.data['Close'], timeperiod=30)
        self.data['ADXR'] = ta.ADXR(self.data['High'], self.data['Low'], self.data['Close'], timeperiod=14)
        self.data['RSI'] = ta.RSI(self.data['Close'], timeperiod=14)
        macd, macdsignal, macdhist = ta.MACD(self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    def leading_indicators(self):
        '''
        Leading indicators are used to predict future price movements. 
        '''
        self.data['CMO'] = ta.CMO(self.data['Close'], timeperiod=14)
        self.data['TSF'] = ta.TSF(self.data['Close'], timeperiod=14)

    def instantaneous_indicators(self):
        '''
        Instantaneous indicators provide a snapshot of the market condition at a specific moment, without considering past data. 
        '''
        self.data['HT_TRENDLINE'] = ta.HT_TRENDLINE(self.data['Close'])
        self.data['TYPPRICE'] = ta.TYPPRICE(self.data['High'], self.data['Low'], self.data['Close'])
        self.data[''] = ta.HT_TRENDMODE(self.data['Close'])

    def volume_indicators(self):
        '''
        Volume indicators are used to analyze trading volume and its relationship with price movements.
        '''
        self.data['MFI'] = ta.MFI(self.data['High'], self.data['Low'], self.data['Close'], self.data['Volume'], timeperiod=14)
        self.data['OBV'] = ta.OBV(self.data['Close'], self.data['Volume'])
        self.data['AD'] = ta.AD(self.data['High'], self.data['Low'], self.data['Close'], self.data['Volume'])

    def volatility_indicators(self):
        '''
        Volatility indicators measure the degree of variation in a financial instrument's price over time.
        '''
        # Bollinger band
        upperband, middleband, lowerband = ta.BBANDS(self.data['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
        self.data['ATR'] = ta.ATR(self.data['High'], self.data['Low'], self.data['Close'], timeperiod=14)
        self.data['ATR'] = ta.NATR(self.data['High'], self.data['Low'], self.data['Close'], timeperiod=14)



        


