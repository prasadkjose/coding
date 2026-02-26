""" Solution Module """
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """
        count = 0
        for i in range(0,32):
            if (1 << i) & test_input:
                count+=1

        return count
