""" Solution Module """
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """
        # [[1, 4, 5], [2, 0 0]]
        [matrix, n] = test_input

        # Sum including the current number
        inc = 0

        # Sum excluding the current number
        excl = 0

        for i in range(0, n):
            cur_max = max(inc, excl)
            inc = excl + max(matrix[0][i], matrix[1][i])
            excl = cur_max

        return max(excl, inc)
