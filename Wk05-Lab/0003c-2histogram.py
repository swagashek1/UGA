"""==============================================================================="""	

"""Plot Two Histograms together"""

import pandas as pd
import matplotlib.pyplot as plt

from util import get_data, plot_data

def compute_daily_returns(df):
	"""Compute and return the daily return values."""
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1
	daily_returns.iloc[0, :] = 0 # set daily returns for row 0 to 0
	return daily_returns
	
def test_run():
	# Read data
	dates = pd.date_range('2021-01-01', '2021-12-31')
	symbols = ['SPY', 'TLT', 'GLD', 'AAPL', 'XOM', 'JPM', 'IBM',
'PYPL']
	df = get_data(symbols, dates)
	
	""" Two separate histograms ==========="""
	# Compute daily returns
	daily_returns = compute_daily_returns(df)
	
	# Plot a histogram
	daily_returns.hist(bins=20) 
	plt.show()

	""" Histograms on the same graph ======"""
	# Compute daily returns
	daily_returns = compute_daily_returns(df)
	
	# Compute and plot both histograms on the same chart
	daily_returns['SPY'].hist(bins=20, label="SPY")
	daily_returns['XOM'].hist(bins=20, label="XOM")
	plt.legend(loc='upper right')
	plt.show()
	
if __name__ == "__main__":
	test_run()

"""==============================================================================="""	
