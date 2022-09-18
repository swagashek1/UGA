import pandas as pd

def test_run():
	#print( "       " )
	# common format of dates in csv files (e.g., yahoo finance). A string with below syntax
	# "pandas" read them in as strings
	# We set a couple of dates here for later use
	start_date	= '2010-01-22'
	end_date 	= '2010-01-26'

	# see what the dates look like
	dates		= pd.date_range(start_date, end_date)

	# -- check the content of the dates variable
	# -- the print formatting string: https://pyformat.info/
	# the real phython 3's f-string: https://realpython.com/python-f-strings/
	print( "\n\n------------  Dates: " )
	print( "{}<".format( dates ) )
	print( ">dates[0]< >dates[1]< >len( dates )<" )
	print( ">{}< >{}< >{}<".format( dates[0], dates[1], len( dates ) ) )

	# create empty data frame - that we can append columns with this specified data frame
	# --- pandas handles time series data if you index frames by dates (instead
	#	of integers (default).
	print( "\n\n------------  Empty Data Frames (df0 by integer, df1 by dates)" )
	df0 = pd.DataFrame() # just the default see what it is # index list (of integers):w
	print( "df0:>{}   {}<".format( df0, type( df0 ) ) )

	df1 = pd.DataFrame( index = dates )
	print( "df1:>{}<".format( df1 ) )

	print( "\n\n------------  Non-Empty Data Frames" )
	# read in prices into another data frame
	# have the API specs readily available
	# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
	# parse_datesbool or list of int or names or list of lists or dict, default False
	#
	#  not to waste disk space use 'symbolic' links for data/ files
	# ln [-sf] [source] [destination]
	#
	df2_SPY = pd.read_csv(
		"data/SPY.csv", 		# file we reading in
		index_col="Date", 		# make this the index column
		parse_dates=True,		# parse 'dates' as index objects
		usecols=['Date', 'Adj Close'],  # need one column for our portfolio project
		na_values=['NaN'] 		# NaN should be not a number
		)
	print( "df2_SPY:\n{}".format( df2_SPY ) )


	# https://pandas.pydata.org/docs/user_guide/merging.html - combining frames
	# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging-join
	print( "\n\n------------  Join Frames - empty column (df1) with csv (df2_SPY) column 1st " )
	dfR=df1.join( df2_SPY ) # NaNs are still in it want to drop it
	print ( dfR )

	print( "\n\n------------  let's drop those NaNs " )
	dfR = dfR.dropna()
	print ( dfR )

	print( "\n\n" )
	print( "\n\n------------  df1.join(df2_SPY) ");
	dfR = df1.join(df2_SPY) # for sanity
	print( dfR )

	print( "\n\n------------  df1.join(df2_SPY, 'inner' ) ");
	dfR = df1.join(df2_SPY,how='inner') # alternate in one swoop`
	print( dfR )			    # intersection

	print( "\n\n------------  df1.join(df2_SPY, 'outer' ) ");
	dfR = df1.join(df2_SPY,how='outer') # outer
	print( dfR )			    # union

	print( "\n\n------------  df1.join(df2_SPY, 'left' ) ");
	dfR = df1.join(df2_SPY,how='left') # left
	print( dfR )			   # left index (parent frame)

	print( "\n\n------------  df1.join(df2_SPY, 'right' ) ");
	dfR = df1.join(df2_SPY,how='right') # rigth
	print( dfR )				# right (parameter)

	print( "\n\n------------  df1.join(df2_SPY, 'cross' ) ");
	dfR = df1.join(df2_SPY,how='cross') # cross
	print( dfR )			#  combines rows with each row of parameter


	## Merge(), join(), concatenate() and compare()
	# IMPORTANT!
	## https://pandas.pydata.org/docs/user_guide/merging.html#

if __name__ == "__main__":
	test_run()
