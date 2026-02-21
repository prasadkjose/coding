""" Solution Module """
from collections import Counter

class Solution:
    """ Solution Class """
    # def run_solution(self, test_input):
    #     """ Solution Method """
    #     [string1, string2] = test_input
    #     # Create a hashmap/dict  of charactes and their frequencies.
    #     str_dict = {}
    #     for char in string1:
    #         if char in str_dict:
    #             str_dict[char] += 1
    #         else:
    #             str_dict[char] = 1

    #     for char in string2:
    #         str_dict[char] -= 1
    #         if str_dict[char] == 0:
    #             del str_dict[char]
    #     print(str_dict)
    #     return len(str_dict) == 0

    # Use Python Counters for simpler Space complexity.
    def run_solution(self, test_input):
        """ Solution Method """
        [string1, string2] = test_input
        return Counter(string1) == Counter(string2)
