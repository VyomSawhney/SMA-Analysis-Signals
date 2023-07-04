import yfinance as yf
import numpy as np
import datetime

stock_symbol = input("Please enter a NYSE stock symbol: ")
days = input("How many days ago do you want to retrace? ")

if not days.isdigit() or int(days) < 0:
    print("Invalid number of days. Please enter a positive integer.")
else:
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=int(days))
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    if data.empty:
        print("Invalid stock symbol or no data available for given dates. Please check your input and try again.")
    else:
        data['10_day_SMA'] = data['Close'].rolling(window=10).mean()
        data['50_day_SMA'] = data['Close'].rolling(window=50).mean()

        data = data.dropna(subset=['10_day_SMA', '50_day_SMA']).copy()

        data['10_day_SMA_derivative'] = data['10_day_SMA'].diff()

        data['Signal'] = np.where((data['10_day_SMA'] > data['50_day_SMA']) & (data['10_day_SMA_derivative'] > 0), 'Long',
                                  np.where((data['10_day_SMA'] < data['50_day_SMA']) & (data['10_day_SMA_derivative'] < 0), 'Short', 'N/A'))

        data.to_csv(f'{stock_symbol}_analysis.csv', index=True)

        print(f"Analysis complete. Results stored in '{stock_symbol}_analysis.csv'")
