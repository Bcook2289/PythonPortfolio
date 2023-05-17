import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy

STOCK_NAME = "EA"
COMPANY_NAME = "Electronic Arts Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
AV_KEY = "VMH1RYKCRVHY8QD4"

av_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": AV_KEY,
}
f_parameters = {
    "function": "OVERVIEW",
    "symbol": STOCK_NAME,
    "apikey": AV_KEY,
}

av_response = requests.get(STOCK_ENDPOINT, params=av_parameters)
av_response.raise_for_status()
stocks = av_response.json()
af_response = requests.get(STOCK_ENDPOINT, params=f_parameters)
af_response.raise_for_status()
overview = af_response.json()

daily_data = stocks['Time Series (Daily)']

df = pd.DataFrame.from_dict(daily_data, orient='index')
df.index.name = 'date'
df.columns = ['open', 'high', 'low', 'close', 'adjusted close', 'volume', 'dividend amount', 'split coefficient']
df = df.drop(['adjusted close', 'dividend amount', 'split coefficient'], axis=1)
df = df.sort_index(ascending=True)

print(df.head())

df['close'] = df['close'].astype(float)
df['MA20'] = df['close'].rolling(window=20).mean().bfill()
df['pct_change'] = (df['close'] - df['MA20'])/df['MA20'] * 100
df['EMA20'] = df['close'].ewm(span=20, adjust=False).mean()
fig, ax = plt.subplots()
ax.plot(df.index, df['close'], label='Closing Price', color='black')
ax.plot(df.index, df['MA20'], label='20-day Rolling Average', color='red')
ax.plot(df.index, df['EMA20'], label='20-day EMA', color='blue')
ax2 = ax.twinx()
ax2.plot(df.index, df['pct_change'], label='Percentage Change (MA20 and Close)', color='green')
ax.set_title(f'Stock Closing Price from {df.index[0]} to {df.index[-1]}')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax2.set_ylabel('Percentage Change')
df.index = pd.to_datetime(df.index)
ax.set_xticklabels(df.index.strftime('%Y-%m-%d'), rotation=45)
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_locator(plt.NullLocator())
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, loc='lower right')
plt.show()
