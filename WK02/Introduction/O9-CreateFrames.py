import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('THREE')

    # create a frame using the content of a dictionary
    # columns: forks, knives, and spoons in different drawers 0,1,2,3
    # rows 0, 1, 2, 3
    # content of each cell in 'list'
    data = {
    'forks':    [2, 4, 6, 8],
    'knifes':   [5, 5, 5, 5],
    'spoons':   [0, 2, 3, 4]
    }
    print(data)

    drawers = pd.DataFrame(data)
    print( drawers )

    #index drawers by name.
    drawers_names = pd.DataFrame(data, index=['Adam', 'Eve', 'Bender', 'Axel'])
    print( drawers_names )

    # access row by name
    print()
    eve_drawer = drawers_names.loc['Eve']
    print( eve_drawer )
# See PyCharm help at https://www.jetbrains.com/help/pycharm/