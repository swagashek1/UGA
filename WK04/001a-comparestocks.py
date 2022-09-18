"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
    for symbol in symbols:
        # 1. read data from symbol
        df_temp = pd.read_csv(symbol_to_path(symbol),
                              index_col='Date',
                              parse_dates=True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan'])

        # 2. rename Adj column column to symbol name
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        # 3. join data with main data frame
        df = df.join(df_temp)

        # 4. drop dates SPY did not trade (where SPY is NaN).
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])
    return df


def plot_data(df, title="Stock prices"):
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    plot_data(df/df.iloc[0,:])


if __name__ == "__main__":
    test_run()
