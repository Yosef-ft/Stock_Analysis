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
        self.data['macd'], self.data['macdsignal'], self.data['macdhist'] = ta.MACD(self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

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
        self.data['HT_TRENDMODE'] = ta.HT_TRENDMODE(self.data['Close'])

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
        self.data['BB_upperband'], self.data['BB_middleband'], self.data['BB_lowerband'] = ta.BBANDS(self.data['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
        self.data['ATR'] = ta.ATR(self.data['High'], self.data['Low'], self.data['Close'], timeperiod=14)
        self.data['NATR'] = ta.NATR(self.data['High'], self.data['Low'], self.data['Close'], timeperiod=14)


    def plot_price_indicators(self, data: pd.DataFrame):
        '''
        Plots indicators that are close to the price
        '''

        fig, ax1 = plt.subplots(figsize=(14, 7))

        # Plot the Close price
        ax1.plot(data.index, data['Close'], label='Close Price', color='blue')

        # Plot the indicators
        ax1.plot(data.index, data['EMA'], label='EMA', color='red')
        ax1.plot(data.index, data['WMA'], label='WMA', color='green')
        ax1.plot(data.index, data['HT_TRENDLINE'], label='HT_TRENDLINE', color='brown')
        ax1.plot(data.index, data['TYPPRICE'], label='TYPPRICE', color='pink')
        ax1.plot(data.index, data['TSF'], label='TSF', color='cyan')

        ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))

        ax1.set_title('Close Price with Indicators')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Value')

        plt.tight_layout()
        plt.show()

    
    def plot_RSI(self, data):
        fig, axes = plt.subplots(nrows=2, figsize=(14, 7))

        # Plot the Close price
        axes[0].plot(data.index, data['Close'], label='Close Price', color='blue')
        axes[0].set_title("Closing price")

        axes[1].plot(data.index, data['RSI'], label='RSI', color='purple')
        axes[1].axhline(y=20, color='red', linestyle='--', label='Oversold (20)')
        axes[1].axhline(y=80, color='green', linestyle='--', label='Overbought (80)')
        
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

        axes[1].set_title('RSI Indicators with 20 and 80 as oversold and overbought lines')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Value')

        plt.tight_layout()
        plt.show()

    def plot_CMO(self, data):
        fig, axes = plt.subplots(nrows=2, figsize=(14, 7))

        # Plot the Close price
        axes[0].plot(data.index, data['Close'], label='Close Price', color='blue')

        axes[1].plot(data.index, data['CMO'], label='CMO', color='gray')
        axes[1].axhline(y=-50, color='red', linestyle='--', label='Oversold (-50)')
        axes[1].axhline(y=50, color='green', linestyle='--', label='Overbought (50)')

        axes[0].set_title("Closing price")
        
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

        axes[1].set_title('CMO Indicator')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Value')

        plt.tight_layout()
        plt.show()

    def plot_MFI(self, data):

        fig, axes = plt.subplots(nrows=2, figsize=(14, 7))

        # Plot the Close price
        axes[0].plot(data.index, data['Close'], label='Close Price', color='blue')
        axes[0].set_title("Closing price")

        axes[1].plot(data.index, data['MFI'], label='MFI', color='magenta')
        axes[1].axhline(y=20, color='red', linestyle='--', label='Oversold (20)')
        axes[1].axhline(y=80, color='green', linestyle='--', label='Overbought (80)')

        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

        axes[1].set_title('MFI Indicator')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Value')

        plt.tight_layout()
        plt.show()

    def plot_OBV(self, data):

        fig, axes = plt.subplots(nrows=2, figsize=(14, 7))

        # Plot the Close price
        axes[0].plot(data.index, data['Close'], label='Close Price', color='blue')
        axes[0].set_title("Closing price")

        axes[1].plot(data.index, data['OBV'], label='OBV', color='yellow')

        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

        axes[1].set_title('OBV Indicator')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Value')

        plt.tight_layout()
        plt.show()


    def plot_AD(self, data):

        fig, axes = plt.subplots(nrows=2, figsize=(14, 7))

        # Plot the Close price
        axes[0].plot(data.index, data['Close'], label='Close Price', color='blue')
        axes[0].set_title("Closing price")

        axes[1].plot(data.index, data['AD'], label='AD', color='darkblue')

        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

        axes[1].set_title('AD Indicator')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Value')

        plt.tight_layout()
        plt.show()     


    def plot_ATR(self, data):

        fig, axes = plt.subplots(nrows=2, figsize=(14, 7))

        # Plot the Close price
        axes[0].plot(data.index, data['Close'], label='Close Price', color='blue')
        axes[0].set_title("Closing price")

        axes[1].plot(data.index, data['ATR'], label='ATR', color='darkgreen')

        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

        axes[1].set_title('ATR Indicator')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Value')

        plt.tight_layout()
        plt.show()                  

    def plot_ADXR(self, data):

        fig, axes = plt.subplots(nrows=2, figsize=(14, 7))

        # Plot the Close price
        axes[0].plot(data.index, data['Close'], label='Close Price', color='blue')
        axes[0].set_title("Closing price")

        axes[1].plot(data.index, data['ADXR'], label='ADXR', color='yellow')
        axes[1].axhline(y=20, color='red', linestyle='--', label='< 20 weak trend')
        axes[1].axhline(y=25, color='green', linestyle='--', label='> 25 stronger trend')

        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

        axes[1].set_title('ADXR Indicator')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Value')

        plt.tight_layout()
        plt.show()        



        
class PortOptimizer:
    def __init__(self):
        pass

