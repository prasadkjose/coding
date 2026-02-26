""" Solution Module """


class Solution:
    """ Solution Class """

    def run_solution(self, test_input: list[list[int], int]):
        """ Solution Method """
        [nums, k] = test_input
        occurance_dict: dict[int, int] = dict()
        result = list()
        for i in nums:
            if i in occurance_dict:
                occurance_dict[i] += 1
            else:
                occurance_dict[i] = 1

            if occurance_dict[i] >= k:
                result.append(i)
        return list(set(result))
