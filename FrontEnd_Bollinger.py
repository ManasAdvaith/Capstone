import pandas as pd
import pandas_datareader as web
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def bands(ticker,end_date):

    bars = web.DataReader(ticker, data_source='yahoo', start='2018-01-01', end=end_date)

    df = pd.DataFrame(bars)
    df['close'] = df.filter(['Close'])

    df['sma'] = df['close'].rolling(20).mean()
    # SD
    df['sd'] = df['close'].rolling(20).std()
    # lower band and Upper band
    df['lb'] = df['sma'] - 2.3 * df['sd']
    df['ub'] = df['sma'] + 1.5 * df['sd']
    df.dropna(inplace=True)

    plt.figure(figsize=(16, 8))
    plt.title('Model')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USE($)', fontsize=18)
    plt.plot(df['close'])
    plt.plot(df['sma'])
    plt.plot(df['lb'])
    plt.plot(df['ub'])
    plt.legend(['close', 'sma', 'lb', 'ub'], loc='lower right')
    plt.show()

ticker=input()
yesterday=datetime.now()-timedelta(1)
end_date=datetime.strftime(yesterday,'%Y-%m-%d')
bands(ticker,end_date)