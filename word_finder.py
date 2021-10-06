#############################################################
# This script is used to find a word in the sentence
# The input is in string format and the output may be tuple or a string
# Author:
# Created at : 10/01/2021
# Last Modified at : 10/01/2021
########################################################################


def main():
    word_sequence = input("Enter the sequence with space separated words: ")
    word_to_search = input("Enter a word to search: ")
    output = search_in_sequence(word_sequence, word_to_search)

    if output is None:
        print("No")
        return

    for i in output:
        print(i)


def search_in_sequence(word_sequence, word_to_search):
    """A function to search a word in the given sequence 

    Args:
        word_sequence (string): A sequence of words
        word_to_search (string): The word which has to searched in the sequence

    Returns:
        tuple: If word is found, returns Yes and word count. it not None.
    """

    word_sequence = word_sequence.lower()
    word_to_search = word_to_search.lower()

    if word_to_search in word_sequence:
        # returns a string and the count inside a tuple
        return "Yes", word_sequence.count(word_to_search)

    return None


if __name__ == "__main__":
    main()
