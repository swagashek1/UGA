
"""Utility functions"""
import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
	"""Return CSV file path given ticker symbol."""
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
	"""Read stock data (adjusted close) for given symbols from CSV files.""" 
	df = pd.DataFrame(index=dates)
	df1 = pd.DataFrame(index=dates)
	#if 'SPY' not in symbols:  # add SPY for reference, if absent
		#symbols.insert(0, 'SPY')

	for symbol in symbols:
		# 1. read data from symbol
		df_temp = pd.read_csv(symbol_to_path(symbol),
			index_col = 'Date',
			parse_dates=True,
			usecols=['Date','Adj Close'],
			na_values=['nan'])

		# 2. rename Adj column column to symbol name
		df_temp = df_temp.rename(columns = {'Adj Close':symbol})

		# 3. join data with main data frame
		#df = df.join(df_temp)
		#df=pd.concat([df, df_temp],axis = 1,join='inner')
		df = df.merge(df_temp,left_index=True,right_on='Date')


		#print( df )

		# 4. drop dates SPY did not trade (where SPY is NaN).
		if symbol == 'SPY':
			df = df.dropna(subset=["SPY"])
		#print( symbol )
	return df

def test_run():
	# Define a date range
	dates = pd.date_range('2021-08-01', '2022-08-1')

	# Choose stock symbols to read
	symbols = ['AAPL','AMZN','GOOG', 'IBM', 'GLD']

	# Get stock data
	df = get_data(symbols, dates)
	df.to_csv('method2.csv', sep=',')
	print( df )

if __name__ == "__main__":
	test_run()

