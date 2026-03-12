"""Solution Module"""


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        [nums, k] = test_input
        print(nums[-k:])
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        return nums
