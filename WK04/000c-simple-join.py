import pandas as pd

def test_run():
	start_date	= '2010-01-22'
	end_date 	= '2010-01-26'

	# create a continious data range (currently unpopulated)
	dates= pd.date_range(start_date, end_date)
	df1 = pd.DataFrame(index=dates)

	df2_SPY = pd.read_csv("data/SPY.csv", index_col="Date",
		parse_dates=True,
		usecols=['Date', 'Adj Close'],
		na_values=['NaN'] # NaN should be not a number
		)


	print( "" )
	print( "frame d1 of all dates in specified range. join frame  ( spy dates )" )
	print( "      dates in range but not in SPY will be NaNs" )
	dfR=df1.join(df2_SPY) # NaNs are still in it want to drop it
	print( dfR )
	print( "d1 all dates in RANGE . join df ( spy dates ) ** ADD dropna()" )
	dfR = dfR.dropna()
	print( dfR )

	print( "do a (inner) join (intersection of dates) instead of dropping NaNs" )
	dfR = df1.join(df2_SPY,how='inner') # alternate
	print( dfR )

	print( "rename column names" )
	dfSPY = dfR.rename(columns={'Adj Close': 'SPY'})
	print( dfSPY )




if __name__ == "__main__":
	test_run()
