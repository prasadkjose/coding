"""Solution Module"""


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        # We can start from 2 as it doesn't matter if 0,0 or 1,1 or 0,1
        # are the first two elements

        k = 2

        for i in range(2, len(test_input)):
            if test_input[i] != test_input[k - 2]:
                test_input[k] = test_input[i]
                k += 1
        return k
