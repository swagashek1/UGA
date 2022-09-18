import csv

# read in file. Get a handle to the file
FILENAME = 'O7-rdu-weather-history.csv'

# GET a file handler -
file_handle = open(FILENAME)
type(file_handle)
#print( type( file_handle) )

# GET a Worker that can read
# position a reader to the file's handle
csvreader = csv.reader(file_handle)

# start parsing the data/rows/columns/cells/titles/indexes
# first create a data structure to store the data
# lets create a list, empty at first.

#stores the list of cells in a 'row'
data_list = []

# now read in a row of ata using csvreader - it points to the beginning
# of the csv file so we just need to tell it to read the 'next' row.
data_list = next( csvreader )

#first row is the header of the file
#print( data_list ) or look in Variable browser in pyCharm

data_list = next( csvreader )
print( data_list )
data_list = next( csvreader )
print( data_list )

# exit(0)

# lets reset handled to the beginning of the file
file_handle.seek(0)

header = []
header = next(csvreader)

# we want to keep ALL rows. - we need to use a list of lists to to that.
# [ [r10, r11, ..., r1n ] , [r20, r21, .... r2n], .....,{rn0, rn2, ... rnn] ]
rows = []
cnt = 0;
for row in csvreader:
	rows.append(row)
	cnt= cnt+1

print("hello")
print( rows[1][1] )
#exit(0)

print("0 ----")
print("0 ----")

#print( rows[5] )
print("1 ----")
print( header )
print("2 ----")
#print( rows[5][1] )
print("3 ----")

# --> ERROR
# print( rows[5][0] )

file_handle.close()