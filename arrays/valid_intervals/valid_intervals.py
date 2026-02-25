""" Solution Module """
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """
        start_time: list = list(map(lambda interval: interval[0], test_input))
        sorted_starts: list = sorted(start_time)
        for index, interval in enumerate(test_input):
            print(index, interval, sorted_starts)
            curr_end_time = interval[1]
            if index == len(start_time):
                return True
            if curr_end_time > sorted_starts[index+1]:
                return False
            return True
