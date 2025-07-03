'''
It is best practice to include comments like this at the top 
of your script to describe what your script does. For longer 
comments, put them inside triple quotes (as I've done here). 
Everything inside the triple quotes will be ignored by Python.

Your comment should explain what the script does and give
any information that someone would need to run the script, 
such as what type of files are required (if any).
----

This script includes two functions:

printMean : take a list as an argument and 
    returns the mean and a sentence as a tuple 

printSum : take a list as an argument and 
    returns the sum and a sentence as a tuple 

To run the script:
First, you must import the functions into a python session or a notebook.
Then you can use either function by sending it a list.  
For example:

from example02_arithmetic import *

my_list = [1,2,3,4,5]
s, s_sentence = print_sum(my_list)
print(s_sentence)

'''

# IMPORT MODULES
# if you have any modules to import, import them at the top of the script,
# under the comments, so that anyone using this script can quickly
# know which modules are required - they might need to install them.
# These are called dependencies.
import numpy as np


# FUNCTION DEFINITIONS
# include any function definitions next
def print_mean(a_list):
    '''Returns the mean of a list, rounded to the hundredths, in a complete sentence.'''
    m = np.mean(a_list)
    return (m, "The mean of the numbers provided is " + str(round(m, 2)) + ".")
	
def print_sum(a_list):
    '''Returns the sum of a list in a complete sentence.'''
    s = np.sum(a_list)
    return (s, "The sum of the numbers provided is " + str(round(s, 2)) + ".")


# MAIN
if __name__ == "__main__":
    print("This code does not run anything by default.  Please import the functions and use them elsewhere.")