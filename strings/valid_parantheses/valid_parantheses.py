""" Solution Module """
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """
        # "()"
        # (
        valid = {
            '}': '{',
            ']': '[',
            ')' : '('
        }
        stack = []
        for char in test_input:
            if len(stack) !=0 and char in valid and stack[-1] == valid[char]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
