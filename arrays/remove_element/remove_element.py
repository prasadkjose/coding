"""Solution Module"""


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        [arr, val] = test_input
        k = 0
        for i, e in enumerate(arr):
            if e != val:
                arr[k] = arr[i]
                k += 1
        return k
