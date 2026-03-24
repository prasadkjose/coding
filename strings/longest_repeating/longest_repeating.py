"""Solution Module"""


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        [s, k] = test_input
        hash_map = {}
        longest = 0

        left = 0
        curr_max = 0

        for right, value in enumerate(s):
            # increase the count of occourance.
            hash_map[value] = 1 + hash_map.get(value, 0)
            curr_max = max(curr_max, hash_map[value])

            while (right - left + 1) - curr_max > k:  # Invalid window
                # decrease the window size(left) since the window is invalid
                hash_map[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest
