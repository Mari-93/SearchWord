
#############################################################
# This Test script is used to Test the search_in_sequence function
# The input is in string format and the output may be tuple or a string
# Author:
# Created at : 10/04/2021
# Last Modified at : 10/04/2021
########################################################################


import unittest

import constants as c
from word_finder import search_in_sequence


class TestWordSequence(unittest.TestCase):

    word_sequence = "Today is toDay and the day is 4"
    word_sequence_with_numbers = "12 2 f r t ty 12 2"

    def test_word_in_sequence(self):

        self.assertEqual(search_in_sequence(
            self.word_sequence, "todaY"), (c.WORD_FOUND, 2))

        self.assertEqual(search_in_sequence(self.word_sequence, "from"), None)

        self.assertEqual(search_in_sequence(
            self.word_sequence, "4"), (c.WORD_FOUND, 1))

        self.assertEqual(search_in_sequence(
            self.word_sequence_with_numbers, "12 2"), (c.WORD_FOUND, 2))


if __name__ == "__main__":
    unittest.main()
