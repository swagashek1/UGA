import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from util import get_data

"""Scatter-plots."""


def plot_scatter( daily_returns, SYMBOL_X, SYMBOL_Y ):
	# Scatter-plot Y vs X
	daily_returns.plot(kind='scatter', x=SYMBOL_X, y=SYMBOL_Y)

	# compute the equation of the (linear) model
	# degree of a linear polynomial is 1 - the third parameter
	linear_model = np.polyfit( daily_returns[SYMBOL_X], daily_returns[SYMBOL_Y], 1 )
	beta 	= linear_model[0]
	alpha 	= linear_model[1]

	print(f" beta of {SYMBOL_Y} = {beta:+.6f}")
	print(f"alpha of {SYMBOL_Y} = {alpha:+.6f}")

	# plot the line using the equation and SYMBOL_X as the independent variable
	plt.plot(daily_returns[SYMBOL_X], beta * daily_returns[SYMBOL_X] + alpha, '-', color='r',label = f"Y={beta:+.6f}X{alpha:+.6f}")
	plt.legend()
	plt.show()

	return beta,alpha


def compute_daily_returns(df):
	"""Compute and return the daily return values."""
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1
	daily_returns.iloc[0, :] = 0  # set daily returns for row 0 to 0
	return daily_returns


def test_run():
	# Read stock data from directory dataT
	# use link:
	# ln -s <SOURCE> <TARGET>
	# ln -s dataZ data
	dates = pd.date_range('2021-01-01', '2021-12-31')

	symbols = ['SPY', 'TLT', 'GLD', 'AAPL', 'XOM', 'JPM', 'IBM',
'PYPL']

	df = get_data(symbols, dates)
	df1 = pd.DataFrame(index=symbols, columns =['alpha','beta'])
	print(df)
	# Compute daily returns - for whole frame
	daily_returns = compute_daily_returns(df)
	for x in range(len(symbols)) :
		beta,alpha=plot_scatter(daily_returns, 'SPY', symbols[x])
		df1.loc[symbols[x],'alpha'] = alpha
		df1.loc[symbols[x], 'beta']= beta
		print(x)
	print(df1)
	# first row are stock correlated with SPY -
	# print the correlation matrix.
	print( daily_returns.corr(method='pearson') )

	
if __name__ == "__main__":
	test_run()

"""==============================================================================="""	
