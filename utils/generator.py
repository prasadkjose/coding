""" Utility module that generates code templates."""

class Generator:
    """Class to generate language specific templates."""
    def get_and_generate_files(self, language: str, is_test: bool)->str:
        if language == 'python':
            return self.generate_python_files(is_test=False)


    def generate_python_files(self, is_test)->str:
        """ Get the file context need to initilize python files
        The indendation looks weird so that the generated file will pass lint checks.
        """
        if is_test is True:
            return """\"\"\"Testing Module\"\"\"
import logging
import importlib
logger = logging.getLogger(__name__)
class Test:
    \"\"\" Test Class \"\"\"
    def test(self, solution_module_path, problem_name):
        \"\"\"Method to test solution\"\"\"
        # Example: arrays.contains_duplicate.contains_duplicate import Solution
        solution_module = importlib.import_module(solution_module_path)
        test_input = []
        solution_class = solution_module.Solution()
        result = solution_class.run_solution(test_input)
        if result is True:
            logger.info("Test Case Passed for %s for %s", problem_name, test_input)
        elif result is False:
            logger.info("Test Case Failed for %s for %s", problem_name, test_input)
        else:
            logger.info("The result is %s", result)
"""


        return """\"\"\" Solution Module \"\"\"
class Solution:
    \"\"\" Solution Class \"\"\"
    def run_solution(self, test_input):
        \"\"\" Solution Method \"\"\"
        return True
"""

    def generate_typescript_files(self, is_test)->str:
        """ Method to generate TypeScript files """
        if is_test is True:
            return """class Solution {
/**
    * @param {string} s
    * @return {boolean}
    */
isPalindrome(s) {}
}"""
