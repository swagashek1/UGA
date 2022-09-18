import pandas as pd
import os
import yfinance as yf
import argparse

## https://docs.python.org/3/library/argparse.html
def symbol_to_path( symbol, base_dir=os.path.join(".", "data" )):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_dataYFSymbol( symbol, dates ):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = yf.download(   symbol,
                        interval="1d",
                        start=dates[0], # first date in range
                        end=dates[-1]   # last date in range
                     )
    return df

if __name__ == '__main__':
    date_start = "2021-07-01"
    date_end  =  "2022-09-05"

    parser = argparse.ArgumentParser(
        prog='0003_Get_Data_YF',
        add_help=True,
        description='Short Sample'
    )

    ## --- https: // docs.python.org / 3 / library / argparse.html
    symbols = ['GLD']

    parser.add_argument('-x', nargs='*', action="store", dest="symbols", default=symbols) # list
    parser.add_argument('-s', action="store", dest="date_start", default=date_start)      # single item
    parser.add_argument('-e', action="store", dest="date_end", default=date_end)
    args = parser.parse_args()
    dates       = pd.date_range( args.date_start, args.date_end )
    symbol      = args.symbols[0]

    print(f"first date {dates[0]} last date {dates[-1]}")
    print(f'symbols = {symbol}')
    print( f"---> Restrit the Date Range Start: = {date_start} to End = {date_end}" )

    datafile = symbol_to_path( symbol )
    df = get_dataYFSymbol(symbol, dates)

    print("Write/geneate a csv file of GOOG, with separator ',':")

    df.to_csv(datafile, sep=',', index=True, encoding='utf-8' )


