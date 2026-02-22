""" Solution Module """
import re
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """
        #"Was it a car or a cat I saw?"
        sanitized_input = re.sub(r'[^a-z]', '', test_input.lower())
        reversed_input = sanitized_input[::-1]
        print(reversed_input)
        print(sanitized_input)
        return sanitized_input == reversed_input
