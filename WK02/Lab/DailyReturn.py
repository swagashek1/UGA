import pandas as pd

def assess_symbol( symbol ):
    # create the name of the .csv file by using f'string.
    # below creates the string "SPY.csv" since the input parameter is the string "SPY"
    data_df = pd.read_csv( f'{symbol}.csv', index_col='Date', parse_dates=True)

    # prints out the first few lines of our file that we just read in.
    print( f"\nFirst few lines of {symbol}:" )

    print( data_df.head() )

    # prints out another sub-range
    begin   = '2022-08-10'
    end     = '2022-08-17'

    # Later you will print out results by restricting rows and columns by using pandas.DataFrame.loc - example are below
    #  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
    print( f'\n{symbol} data from {begin} to {end}:\n{data_df.loc[begin:end]}' )
    print( f'\n{symbol} Open & Close columns only from {begin} to {end}:\n{data_df.loc[begin:end][["Open","Close"]]}' )

    # Add an empty column to separate our original raw data from computed data, title/name of column is "--- Blank ---"
    data_df["--- Blank --- "] = ""

    # -------------------------
    # In this lab you will calculate the rate of daily return,
    # both intra- and inter-day returns.
    # The Formula is below:
    #   (current_price - yesterday_price)/ yesterday_price
    #
    # It simplified below it to make simpler to calculate in python, as follows:
    #   current_price/yesterday_price - yesterday_price/yesterday_price
    #   current_price/yesterday_price - 1
    #
    # IN the downloaded CSV file SPY.csv -- the order of rows are ordered from rows 0, to 1 so that the
    # oldest row is on top (has lower row numbers), and more recent dates are lower (has higher row numbers)
    #   .
    # Example: Lets us consider row 4 (6/23/2022)- to be our "current" closing price - the previous price or
    # yesterday's price is on the row above. - to add column that has yesterday's price on the same row as
    # In order compute the daily return we will create a copy of the
    #  close column and then shift it 'down' by one row (or cell) the added as a new column to our sheet.
    #  In the provided Excel Sheet - that process is demonstrated in Column "J".
    #
    #  Note here almost all rows in the Excel sheet has both it's current closing price, and yesterday
    #  Closing price on its same row. Except for the top row - row 6/21/22 (row 2), and row 46 not date
    #   here as only the shifted columns reside in this row.
    #
    # In Python, Let's first create a title string for the row - just like the one in the Excel workbook,
    # we will store the title string in a variable named + "shifted"
    shifted =  "Close.shift(1)"

    # Let's create standalone Pandas Series - that is a copy of the Close column but shifted down by 1 'row'.
    # SEE:
    #   https://www.tutorialspoint.com/how-to-shift-a-column-in-a-pandas-dataframe
    # on how to do this. Use the variable' shifted' to append this column to our 'data_df' Dataframe.
    #  data_df[shifted] = XXX.
    #

    # --> TASK 1.
    # MODIFY: Replace 'Volume' below with appropriate Columns and shift function.
    print("task 1")
    data_df[shifted] = data_df.Close.shift(1)
    # -->  print(f"data type = {type(data_df[shifted])}")

    # print the result on the terminal --> .loc to Specify rows and  columns as demonstrated above.
    # print out the two columns "Close" AND the new Column given by 'shifted' from begin and end dates.

    # --> TASK 2.
    # MODIFY: the below print() to print the dates form begin to end, and print columns: Close and shifted'
    print("task 2")
    print( f' {symbol} Close & Shifted Close from {begin} to {end} is:\n{data_df.loc[:][["Close", shifted]]}' )
    print("task 2")
    # -->

    # As a side note select specific columns with a list ["Close", shifted] on the full'index' but then apply head()
    # to restrict or filter the output
    df2 = data_df.loc[:,["Open", "Close"]].head()
    print( f'\n\n{symbol} Open & Close from :\n{df2}' )

    # Create a label for a variable 'inter_day' that contains the title of the column.
    inter_day =  "Inter Day Return"

    # inter_daily_return   = ( current_price/yesterday_price - 1 ) * 100
    # current_price -> specify the "Close" column
    # yesterday_price --> specify the shifted column that we created above. then subtract 1, and multiply by 100

    # ---> TASK 3.
    # MODIFY: Replace the below 'Volume' with the appropriate computation outlined above.
    print("task 3")
    data_df[inter_day] = (data_df["Close"]/data_df[shifted]-1)*100
    # --->

    # prints out the 'head' of Close column, the shifted column, and the inter_day column outlined above
    df3 = data_df.loc[:,["Close", shifted, inter_day]].head()
    print( f' {symbol} {inter_day} :\n{df3}' )

    # Calculate the *means) for both inter- and intraday returns --   In the mean only include rows that have both
    # the previous close and the current close on the same row, i.e., exclude the
    #  --> top row, and the bottom row.
    # NOTE that when we created our 'shifted' column - the first row 6/21 does not contain 'both' the current
    # price and 'yesterday' price. So the first row that has complete data is 6/22, the last
    # day is still '8/22'. Let us create two 'new' variable called, 'start' and 'stop' containing the range of
    # rows WITH complete data
    start       = '2022-06-22'
    stop        = '2022-08-22'

    # Use pandas mean() to calculate the mean of the inter_day column', pandas has a mean() function both for frames,
    # and for Series (just the columns). IN essense a pandas data frame is a bunch of columns or Series
    # you may need to use .loc to restrict the index (dates).
    # For the above mean, name its variable 'inter_day_mean'
    # Sketched out formula for the mean() should look something like the below:
    #
    #  inter_day_mean = DataFrame.loc[INDEX0:INDEX1][ COLUMN-NAME ].mean()

    # ---> TASK 4:
    # MODIFY:
    # replace the fake mean: 0.7777 with correct usage of mean(). see above outline.
    inter_day_mean = data_df.loc[start:stop][ inter_day ].mean()
    # --->
    #
    print( f'\n{inter_day_mean}' )

    # Now we return to intra daily return - that is using open and close prices on the same day.
    # create title for this new column.
    intra_day   = "Intra Day Return"

    # Formula below:
    # intraReturn=  (Close Price - Open Price)/Open * 100
    # store the Intra Day Return computation of the columns: Open & Close and store
    # it in variable: intraReturn -
    #
    # in the below complete the computation as described above.

    # ---> TASK 5
    # MODIFY:
    # Modify the below computation to the computation as described above (replace "Volume')
    print("task 5")
    intraReturn = ((data_df["Close"] - data_df["Open"])/data_df["Open"])*100  # Replace Volume with appropriate computation outlined above,

                                          # no shifting is required here.

    # --->

    # insert the new Column "intraReturn - in proper place in the DataFrame, see below:
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html
    #   DataFrame.insert(loc, column, value, allow_duplicates=False)
    # Column number starts at position '0' for the A Column in Excel.
    # Example insert at column 1, would insert column after the A column, and
    # we do allow Duplicates.
    #
    # Insertion should look something like this: fill in XX and XXXX
    # data_df.insert(XX, intra_day, XXXX , True)
    #

    # ---> TASK 6
    # MODIFY:
    # replace below '1' for location so that it resembles the provided Excel sheet, and
    # replace '55' with the intraReturn computed further abovel
    # computed above.
    # --->
    data_df.insert( 1, intra_day, intraReturn , True )
    # --->


    print( f'\n{symbol} data from {begin} to {end}:\n{data_df.loc[begin:end]}' )
    print( f' {symbol} RA open & close from {begin} to {end} is:\n{data_df.loc[begin:end][["Open","Close",intra_day]]}' )

    # ---> TASK 7
    # MODIFY:
    # compute the average of teh intraday return column, - replace 0.8888 with correct usage of mean(), use the
    # same process as mean of inter-day return columns intra_day column.
    # --->
    intra_day_mean = data_df.loc[start:stop][ intra_day ].mean() # replace 0.888 appropriately
    # --->

    # and here are our results again. should be the same as the provdided workbook
    print( f'\nInter Day Mean {inter_day_mean}' )
    print( f'\nIntra Day Mean {intra_day_mean}' )

    # data_df.to_csv("c:/tmp/full path.csv", index=False)
    data_df.to_csv("daily_return.csv", index=True)
    return data_df['Close'].max()

def test_run( symbols ):
    """ Function Called from main """
    for symbol in symbols:
        print( f'\nMax Close is:\t\t{assess_symbol(symbol) }')

if __name__ == '__main__':

    symbols = ['SPY']

    test_run(symbols)
