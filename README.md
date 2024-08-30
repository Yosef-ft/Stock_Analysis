# Financial News and Stock Market Correlation Analysis
## Project Overview
This project focuses on analyzing a large dataset of financial news to discover correlations between news sentiment and stock market movements. The analysis is conducted to enhance predictive analytics capabilities, significantly boosting financial forecasting accuracy and operational efficiency at Nova Financial Solutions.

## Objectives
**Sentiment Analysis:** Perform sentiment analysis on financial news headlines to quantify the tone (positive, negative, or neutral) associated with various stock symbols.
**Correlation Analysis:** Establish statistical correlations between sentiment scores derived from news articles and corresponding stock price movements. This involves tracking stock price changes around the publication date of the articles and analyzing the impact of news sentiment on stock performance.

# Key Tasks
1.Descriptive Statistics:
* Analyze textual lengths and publication frequency.
* Count the number of articles per publisher.
  
2.Text Analysis (Sentiment Analysis & Topic Modeling):
* Sentiment analysis on headlines.
* Topic modeling to identify common keywords and phrases. And used word cloud to visualize the topics

3.Time Series Analysis:
* Analyze publication frequency over time.
* Identify seasonal patterns and effects in news publication.
* Examine the impact of news timing on market movements.
  
4.Quantitative Analysis Using TA-Lib:
* Load stock price data and apply various technical indicators.
  * Classified the indicators as:
    * Lagging indicator: EMA, WMA, ADXR, RSI, MACD
    * Leading indicaror: CMO, TSF
    * Instantaneous indicators: HT_TRENDLINE, TYPPRICE
    * Volume indicators: MFI, OBV, AD
    * Volatility indicators: ATR, NATR, Bollinger bands
**Future Word:** Calculate which category of technical indicators is most affected by news sentiment.

## Getting Started
Clone the repository: git clone [repository](https://github.com/Yosef-ft/Stock_Analysis)
Install required packages: 
```python 
pip install -r requirements.txt
```

### Running the Analysis:
- Execute the EDA notebook and Quantitative_analysis notebook for sentiment analysis, topic modeling and quantitative analysis.

## Dependencies:
- [Ta-lib](https://pypi.org/project/TA-Lib/)
