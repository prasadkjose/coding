""" Solution Module """


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        max_vol = 0

        left = 0
        right = len(test_input) - 1

        def check_and_update(left, right):
            curr_max = min(test_input[left], test_input[right]) * (right - left)
            return max(curr_max, max_vol)

        while left < right:
            max_vol = check_and_update(left, right)
            if test_input[left] <= test_input[right]:
                left += 1
            else:
                right -= 1

        return max_vol
