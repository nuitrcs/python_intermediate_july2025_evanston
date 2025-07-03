'''

This script converts plot size from length, width to acres.

This script takes a comma-separated file with an address or 
other identifier in the first column, plot width in feet in 
the second column, and plot length in feet in the third column.


To run the script:
This script is intended to run from the command line.  You must
supply a file name as an argument after the script name.
For example:

python example04b_acre.py plots_of_land_1.csv


'''

import sys
import pandas as pd


def length_width_to_acres(length, width):
    # this function takes the length and width of a plot of land, both in units of feet
    # and returns the acreage, rounded to the nearest hundredth
    sqft = length * width
    acres = sqft / 43560
    return round(acres, 2)
    


if __name__ == "__main__":
    try:
        # get the filename from the command-line (to avoid having to hard-code it)
        csv_file_name = sys.argv[1]

        # read in the file
        df = pd.read_csv(csv_file_name)
        for index, row in df.iterrows():
            acres = length_width_to_acres(row['length_ft'], row['width_ft'])
            print(row['address'] + " is " + str(acres) + " acres.")
    except:
        print('ERROR: Please provide a valid filename.')



