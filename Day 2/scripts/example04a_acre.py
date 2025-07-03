'''

This script converts plot size from length, width to acres.

This script takes a comma-separated file with an address or 
other identifier in the first column, plot width in feet in 
the second column, and plot length in feet in the third column.


To run the script:
This script is intended to run from the command line.  
For example:

python example04a_acre.py


'''

import pandas as pd


# HARD-CODED VARIABLES
# assign any variables, including filenames, here, so that if you want to
# run the script with different data, it's easy to see and change
csv_file_name = "plots_of_land_1.csv"


def length_width_to_acres(length, width):
    # this function takes the length and width of a plot of land, both in units of feet
    # and returns the acreage, rounded to the nearest hundredth
    sqft = length * width
    acres = sqft / 43560
    return round(acres, 2)
    


if __name__ == "__main__":
    # read in the file
    df = pd.read_csv(csv_file_name)
    for index, row in df.iterrows():
        acres = length_width_to_acres(row['length_ft'], row['width_ft'])
        print(row['address'] + " is " + str(acres) + " acres.")

