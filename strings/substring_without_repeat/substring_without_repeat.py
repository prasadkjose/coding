"""Solution Module"""


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        hash_map = {}
        left = 0
        longest = 0
        for right, char in enumerate(test_input):
            if char in hash_map:
                left = max(hash_map[char] + 1, left)
            hash_map[char] = right
            longest = max(longest, right - left + 1)
            print(hash_map, left, right, longest)
        return longest
