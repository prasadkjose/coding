""" Solution Module """


class Solution:
    """ Solution Class """

    def run_solution(self, test_input):
        """ Solutio method"""
        sorted_list = sorted(list(set(test_input)))
        print(sorted_list)
        if len(test_input) == 0:
            return 0

        longest = 1
        current = 1

        for i, num in enumerate(sorted_list):
            if num-sorted_list[i-1] == 1:
                current += 1
            else:
                current = 1

            longest = max(longest, current)

        return longest
