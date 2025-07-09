'''
This script includes three functions that analyze words in a file:

findLongestWord : take a list of words as an input argument and 
    returns the longest word from that list

countVowelWords : takes a list of words as an input argument and 
    returns the number of words from that list that start with a vowel

makeUpperCase : takes a list of words as an input argument and
    returns a list of the same words but in all upper case


To run the script:
You can either import the function into a python session or a notebook.
For example:

from POSSIBLE_SOLUTION_word_analysis import *

Then you can use any of the functions as you wish.
(See the bottom of this file for a code example.)

OR

You can run this code from the command line with 

python POSSIBLE_SOLUTION_word_analysis.py -f words.txt

'''

import argparse

def findLongestWord(words):
    '''
    This returns the longest word from a list of input words.
    the argument words is expected to be a list of strings
    '''
    longest = max(words, key=len)
    return longest

def countVowelWords(words):
    '''
    This returns the number of words from a list of input words that begin with a vowel.
    the argument words is expected to be a list of strings
    '''
    vowels = 'aeiou'
    n_starts_with_vowel = 0
    for word in words:
        if (word[0].lower() in vowels):
            n_starts_with_vowel += 1
    return n_starts_with_vowel

def makeUpperCase(words):    
    '''
    This returns the list of input words in upper case.
    the argument words is expected to be a list of strings
    '''
    uppercase_words = []
    for word in words:
        uppercase_words.append(word.upper())
    return uppercase_words
    
if __name__ == "__main__":

    # define the argument parser
    parser = argparse.ArgumentParser(description="A script to manipulate words from a file.")
    parser.add_argument("--filename", "-f", type=str, default=None, help="Input filename, including full path.")
    
    # BONUS: add another argument defining the number of upper case words to print
    parser.add_argument("--n_upper", "-n", type=int, default=1000, help="Number of upper case words to print")

    args = parser.parse_args()


    try:
        # read in the file and create our list of words
        words = []
        with open(args.filename, 'r') as file:
            file_contents = file.readlines()
        for line in file_contents:
            words.append(line.strip())

        # use the functions above, sending words as the input argument
        longest = findLongestWord(words)
        nvowels = countVowelWords(words)
        ucase = makeUpperCase(words)

        # print the output in full sentences
        print('The list of words you selected is below.')
        print(words)
        print('\nThe longest word in the list is ' + longest + '.\n')
        print('There are ' + str(nvowels) + ' words in the list that start with a vowel.\n')
        print('Below are words from the input list in uppercase:')
        for i,u in enumerate(ucase):
            # BONUS: stop if we've reached the user defined limit
            if (i == args.n_upper):
                break
            print(u)

    except Exception as e:
        print('An error occured: ', e)



