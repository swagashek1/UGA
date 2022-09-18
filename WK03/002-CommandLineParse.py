import pandas as pd
import argparse

## --- https: // docs.python.org / 3 / library / argparse.html
# initialize parser
parser = argparse.ArgumentParser(
    prog='002-CommandLineParse',
    add_help=True,
    description='Short Sample'
)

symbols = ['GOOG']
date_start = '2022-08-01'
date_end = '2022-08-15'
parser.add_argument('-x', nargs='*', action="store", dest="symbols", default=symbols)  # list
parser.add_argument('-s', action="store", dest="date_start", default=date_start)  # single item
parser.add_argument('-e', action="store", dest="date_end", default=date_end)

# parse  the command line.
args = parser.parse_args()
dates = pd.date_range( args.date_start, args.date_end ) # add to pandas date data structure
symbols = args.symbols

print(f"first date {dates[0]} last date {dates[-1]}")
symbol = symbols[0]
print(f'symbol = {symbol}')
print(f'symbols = {symbols}')
print(f"---> Date Range Start: = {date_start} to End = {date_end}")