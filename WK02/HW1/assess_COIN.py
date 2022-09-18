import pandas as pd

def assess_symbol( symbol ):
    # create the name of the .csv file by using f'string.
    # below creates the string "SPY.csv" since the input parameter is the string "SPY"
    data_df = pd.read_csv( f'{symbol}.csv', index_col='Date', parse_dates=True)

    # prints out the first few lines of our file that we just read in.
    print(f"\nAverage Adjusted Close of {symbol}:")
    print(data_df["Adj Close"].mean())
    #daily return= close today-close adj yesterday)/close adj yesterday)*100
    shifted = "Adj Close.shift(1)"
    data_df[shifted] = data_df["Adj Close"].shift(1)
    daily_return = "daily return"
    data_df[daily_return] =  ((data_df["Close"]-data_df[shifted])/data_df[shifted])*100
    print( f"\nDaily Return of {symbol}:" )
    print(data_df[daily_return].mean())

    print( data_df )

    # prints out another sub-range
    begin   = '2021-11-02'
    end     = '2022-06-01'

    # Later you will print out results by restricting rows and columns by using pandas.DataFrame.loc - example are below
    #  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html




def test_run( symbols ):
    """ Function Called from main """
    for symbol in symbols:
        print( f'{assess_symbol(symbol) }')

if __name__ == '__main__':

    symbols = ['COIN']

    test_run(symbols)
