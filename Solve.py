import os, random, math, time, csv, fileinput
from os import listdir
from os.path import isfile, join

# Set CSV file paths
unsolved = [f for f in listdir(os.getcwd()+"\\Puzzles\\unsolved\\") if isfile(join(os.getcwd()+"\\Puzzles\\unsolved\\", f))]
solved = [f for f in listdir(os.getcwd()+"\\Puzzles\\solved\\") if isfile(join(os.getcwd()+"\\Puzzles\\solved\\", f))]


# Function to print the data array on the console
def console_print(puzz):
    print('┎─────────────────────────────┒')
    for i in puzz:
        if puzz.index(i)==3 or puzz.index(i)==6:
            print('┠─────────────────────────────┨')
        print('┃   '+str(''.join(i[1:4]))+'   ┃   '+str(''.join(i[4:7]))+'   ┃   '+str(''.join(i[7:10])),end='   ┃\n')
    print('┖─────────────────────────────┚')


# Initial Column Row test (Validate if a given cell can be solved using the information in the column and row)
def clumn_validation(data,column):
    actual=[]
    missing=[]
    for i in range(9):
        actual.append(int(data[i][column+1][0]))
    for x in range (9):
        if (x+1) not in actual:
            missing.append(x+1)
    return missing




def main():
    curr_puzz = []
    for file in unsolved:
        # Covert the CSV file to a data array
        with open(os.getcwd() + "\\Puzzles\\unsolved\\" + file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                curr_puzz.append(row)
            # Pop header row
            curr_puzz.pop(0)
        print("----- "+file+" -----")
        print(clumn_validation(curr_puzz,1))
        console_print(curr_puzz)
        curr_puzz = []



if __name__ == "__main__":
    main()

