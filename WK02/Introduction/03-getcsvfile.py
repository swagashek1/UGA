import csv

def csv_print_name_number(name, anumber):
    # Use a breakpoint in the code line below to debug your script.
    fname = "csv_print_name_number"
    print(f'[{fname}]: Hi ->{name}<- Get A File number = {anumber}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("over HERE")
    with open('03-hameggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in spamreader:
            print(', '.join(row))
            cnt=0
            for column in row:
                    print(f'\t{cnt}: {column}')
                    cnt+=1
        csv_print_name_number('CSV File Reader', 10)



