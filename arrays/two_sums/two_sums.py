""" Solution Module """
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """
        [nums, target] = test_input
        obj = {} # this will store the {diff: index}
        # Enumerate creates key/value for value and index [[1,2,5,3,7], 7]
        for index, value in enumerate(nums):
            diff = target - value
            # If the difference exists already in the hashMap we have both of our indices.
            if diff in obj:
                return [obj[diff], index]
            obj[value] = index
