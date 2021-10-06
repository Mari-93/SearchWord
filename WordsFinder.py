#############################################################
# This script is used to find a word in the sentence
# The input is in string format and the output may be tuple or a string
# Author:
# Created at : 10/01/2021
# Last Modified at : 10/01/2021
########################################################################




def search_in_sequence(word_sequence, search_word):   # A Function to search the word in the sequence
    """A function to search a word in the given sequence 

    Args:
        word_sequence ([string]): [A sequence of words]
        search_word ([string]): [The word which has to searched in the sequence]

    Returns:
        [type]: [string or Tuple]
    """

    lower_word_sequence = word_sequence.lower()
    lower_search_word = search_word.lower()
    if lower_search_word in lower_word_sequence:
        return "Yes", lower_word_sequence.count(lower_search_word) #returns a string and the count inside a tuple
    else:
        return "No" #returns a string

def main():
    the_sequence = input("Enter the sequence with space separated words: ")
    word_to_search = input("Enter a word to search: ")
    output = search_in_sequence(the_sequence, word_to_search)
    
    if type(output) is str:   # if - for printing the output is the desired format
        print(output)
        
    else:
        for i in output:
            print(i)
 


if __name__ == "__main__":
    main()
