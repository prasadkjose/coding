""" Solution Module """
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """
        # [7,1,5,3,6,4] - Maximise difference - O(n)
        max_diff = 0
        curr_diff = 0
        for index, current in enumerate(test_input):
            unseen_arr = test_input[index+1:]
            for unseen in unseen_arr:
                curr_diff = unseen - current
                max_diff = max(max_diff, curr_diff)
        return max_diff
