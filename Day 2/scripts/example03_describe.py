'''
This script includes one function:

describeData : take a pandas DataFrame as an argument and 
    prints a description of the data


To run the script:
You can run this script from the command line with:

python example03_describe.py

Alternatively, you can make use of the describe_data function either
from the command line or within a notebook, by importing the function:

from example03_describe import *

Then you can use the describe_data function by sending it a pandas DataFrame.
(See the bottom of this file for a code example.)
'''

import pandas as pd

def describe_data(df):
    '''
    This function prints a basic description of a DataFrame.
    the argument df is expected to be a pandas DataFrame
    '''

    print("The first 10 rows of the provided DataFrame:")
    print(df.head(10))
    print("\nSummary statistics:")
    print(df.describe())


if __name__ == "__main__":
    # Create a basic dataframe for testing
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Score": [85, 92, 78]
    }
    df = pd.DataFrame(data)
    describe_data(df)