"""Solution Module"""


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        [nums, k] = test_input
        sorted_list = sorted(nums)

        return sorted_list[k - 1]
