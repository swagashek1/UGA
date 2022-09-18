import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def dotspace():
    print("\n.")

def warmup_tutorial(data):
    # reads in csv - data into a pandas frame for review -  only
    dotspace()
    print(" 01: ----- ")
    print(data)
    dotspace()
    print(" 02: ----- ")
    print(data.columns)
    dotspace()
    print(" 03: ----- ")
    print(data.date)
    dotspace()
    print(" 04: ----- ")
    print(data.temperaturemin)
    dotspace()
    print(" 05: ----- ")
    print(data.temperaturemax)

    ## print( data[5][0] )    ## can't access cells like this -- doesn't work - why?
    ## print(data[[0,1]])     ## can't access cells like this -- doesn't work - why?
    # --> Answer is here: https://pandas.pydata.org/docs/user_guide/indexing.html

    dotspace()
    print(" 06: ----- ")
    print(data[:5])

    dotspace()
    print(" 07: ----- ")
    print(data.loc[2:3])

    dotspace()
    print(" 08: ----- ")
    print(data.loc[0])

    ## continue practicing --
    ## https://pandas.pydata.org/docs/user_guide/indexing.html
    dotspace()
    print(" 09: ----- ")

    print(data['temperaturemin'])

    # write DATA after modifying
    # index - removes the index numbers (0, 1, 2, ... )
    # data.to_csv("write_data.csv", index=False )

    # plotting data - just a quick intro
    ## ax = data.plot(fontsize=12, y=['temperaturemin', 'temperaturemax'])
    ## plt.show()
    # ---- review - end -------------------------------------------------------


# we may test out the autograder - this is a placeholder
def test_code():
    print("")

    # ---- review - begin -------------------------------------------------------
    data = pd.read_csv('04c-rdu-weather-history.csv')

    ## uncomment for simple review on pandas slices
    ## warmup_tutorial(data)

    # START - LAB
    dotspace()
    print("**** ------- *****  ------- *****  ------- ***** ------- ***** ------- *****  ------- *****")
    print("**** ------- *****  ------- *****  ------- ***** ------- ***** ------- *****  ------- *****")
    dotspace()

    print("  Task 1 a ----- mean of temperaturemin no []  : ", end="")

    # for each part of Task 1:
    # replace content of result with proper eqution, and format teh print() so it only prints 4 digits
    # after decimal
    result = data['temperaturemin'].mean()
    print(f"{result:.4f}")
    # print( f"{data.temperaturemin.mean():.4f}")

    print("  Task 1 b ----- mean of temperaturemin    []  : ", end="")
    result = data.temperaturemin.mean()
    print(f"{result:.4f}")

    print("  Task 1 c ----- mean of temperaturemax no []  : ", end="")
    result = data['temperaturemax'].mean()
    print(f"{result:.4f}")

    print("  Task 1 d ----- mean of temperaturemax    []  : ", end="")
    result = data.temperaturemax.mean()
    print(f"{result:.4f}")

    ##  https://pandas.pydata.org/docs/user_guide/indexing.html
    ##  https://pandas.pydata.org/docs/user_guide/10min.html
    # iloc[row indexer, column indexer]
    # double brackets - when you pass in a list to indexer operator [].
    #  ---> Is so you can pass a list of columns to [] to select columns in that order.

    # Task 2. : Use iloc() or loc() to select (and print) a slice as follows.
    # print a slice so that its rows include 10/17/09, 11/3/9
    # and  columns to include temperaturemax & precipitation
    dotspace()
    print("  Task 2 a: ---- slice    : ")
    # print visual -
    # replace result with the slice using iloc
    result = data.loc[[3,5], ['temperaturemax','precipitation']]
    print(f"{result}")

    dotspace()
    print("  Task 2 b: ---- mean each column    : ")
    result = data.loc[[3,5], ['temperaturemax','precipitation']].mean()
    print(f"means for each column:\n{result}")

    ## print(data.head(2))
    # Task 3. :
    #
    dotspace()
    print("  Task 3  : ---- eval difference    : ")
    # use eval() here. note you will change it in place so data now contains the xtra column.
    df = pd.DataFrame({'temperaturemax': data.loc[:,'temperaturemax'],'temperaturemin': data.loc[:,'temperaturemin']})
    df1=data.eval('temparturediff= temperaturemax-temperaturemin');
    print(df1.head(4)) # no difference until you add eval()


    # Task 4. :
    #
    dotspace()
    print("  Task 4 a: filter temperaturemin & temperaturemax")

    min = 50
    max = 75

    # create filter_value here using np.where()
    filter= np.where((max>=data['temperaturemax']) & (data['temperaturemin']>=min))
    print(data.iloc[filter])
    dotspace()

    print("  Task 5  : change 6th row's minimum temp from 55.9 to 50.0")
    # user at() to modify a specific location.
    print("something ... head(4) ...")
    data.at[6, 'temperaturemin']=50.0
    output = data.at[6,'temperaturemin']
    print(output)
    df1 = data.eval('temparturediff= temperaturemax-temperaturemin');
    print(df1.iloc[filter])  # no difference until you add eval()
    df1.iloc[filter].to_csv('test1.csv', sep=',')


if __name__ == "__main__":
    test_code()




