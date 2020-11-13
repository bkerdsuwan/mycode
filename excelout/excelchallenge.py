#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# Request data from user
def get_data():
    input_col1 = input("\nCol1? ")
    input_col2 = input("Col2? ")
    input_col3 = input("Col3? ")
    input_col4 = input("Col4? ")

    d = {"Col1": input_col1, "Col2": input_col2, "Col3": input_col3, "Col4": input_col4}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or \
    enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

while(True):
    filename = input("\nWhat is the name of the *.xls file? ")

    try:
        pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')
        print("The file " + filename + ".xls should be in your local directory")
        break
    except:
        print("That filename is invalid, try a different one?")
