"""Solution Module"""


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        sorted_arr = sorted(test_input)
        result: [[]] = []

        for idx, val in enumerate(sorted_arr):
            if val > 0:
                break

            left = idx + 1
            right = len(sorted_arr) - 1

            while left < right:
                sumed = val + sorted_arr[left] + sorted_arr[right]

                if sumed > 0:
                    right -= 1
                elif sumed < 0:
                    left += 1
                else:
                    result.append([val, sorted_arr[left], sorted_arr[right]])
                    right -= 1
                    left += 1
                    while left < right:
                        left += 1
        return result
