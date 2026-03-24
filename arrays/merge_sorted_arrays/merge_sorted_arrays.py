"""Solution Module"""


class Solution:
    """Solution Class"""

    def run_solution(self, test_input):
        """Solution Method"""
        [nums1, nums2, m, n] = test_input
        i = m - 1
        j = n - 1
        right = (n + m) - 1

        while j >= 0:
            print(i, j, right, nums1)
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[right] = nums1[i]
                i -= 1
            else:
                nums1[right] = nums2[j]
                j -= 1
            right -= 1

        return nums1
