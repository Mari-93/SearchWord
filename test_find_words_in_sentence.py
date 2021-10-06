
#############################################################
# This Test script is used to Test the search_in_sequence function
# The input is in string format and the output may be tuple or a string
# Author:
# Created at : 10/04/2021
# Last Modified at : 10/04/2021
########################################################################


import unittest
from word_finder import search_in_sequence


class WordSequence_test(unittest.TestCase):

    def test_word_in_sequence(self):
        word_sequence = "Today is toDay and the day is 4"
        word_sequence_1 = "12 2 f r t ty 12 2"
        search_word_4 = "12 2"
        search_word_1 = "todaY"
        search_word_2 = "from"
        output_1 = search_in_sequence(word_sequence, search_word_1)
        self.assertEqual(output_1, ("Yes", 2))
        output_2 = search_in_sequence(word_sequence, search_word_2)
        self.assertEqual(output_2, "No")
        search_word_3 = "4"
        output_3 = search_in_sequence(word_sequence, search_word_3)
        self.assertEqual(output_3, ("Yes", 1))
        output_4 = search_in_sequence(word_sequence_1, search_word_4)
        self.assertEqual(output_4, ("Yes", 2))


if __name__ == "__main__":
    unittest.main()