""" Solution Module """
class Solution:
    """ Solution Module """
    # def run_solution(self, nums):
    #     """ Solution Method """
    #     array = []
    #     for num in nums:
    #         if num in array:
    #             return True
    #         array.append(num)
    #     return False

    # Using Hash Set and length
    def run_solution(self, nums):
        """ Solution Method """
        array = set(nums)
        if len(nums) != len(array):
            return True
        return False
