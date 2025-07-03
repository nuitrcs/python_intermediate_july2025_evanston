'''

This script converts plot size from length, width to acres.

This script takes a comma-separated file with an address or 
other identifier in the first column, plot width in feet in 
the second column, and plot length in feet in the third column.


To run the script:
This script is intended to run from the command line.  You must
supply a file name as an argument after the script name.
For example:

python example04c_acre.py -f plots_of_land_1.csv


'''

import argparse
import pandas as pd


def length_width_to_acres(length, width):
    # this function takes the length and width of a plot of land, both in units of feet
    # and returns the acreage, rounded to the nearest hundredth
    sqft = length * width
    acres = sqft / 43560
    return round(acres, 2)
    


if __name__ == "__main__":

    # define the argument parser
    parser = argparse.ArgumentParser(description="A script to calculate acres from land length and width, both in units of feet, as provided in an input csv file.")
    # add any arguments you want (here we have only one)
    parser.add_argument("--filename", "-f", type=str, default=None, help="Input filename, including full path.")

    try:
        # get the user-defined arguments arguments 
        args = parser.parse_args()
        
        # read in the file
        df = pd.read_csv(args.filename)
        for index, row in df.iterrows():
            acres = length_width_to_acres(row['length_ft'], row['width_ft'])
            print(row['address'] + " is " + str(acres) + " acres.")
    except ValueError:
        print('ERROR: Please provide a valid filename.')



