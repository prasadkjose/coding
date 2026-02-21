"""Testing Module"""
import logging
import importlib
logger = logging.getLogger(__name__)
class Test:
    """ Test Class """
    def test(self, solution_module_path, problem_name):
        """Method to test solution"""
        # Example: arrays.contains_duplicate.contains_duplicate import Solution
        solution_module = importlib.import_module(solution_module_path)
        test_input = ['racecar', 'carrace']
        solution_class = solution_module.Solution()
        result = solution_class.run_solution(test_input)
        if result is True:
            logger.info("Test Case Passed for %s for %s", problem_name, test_input)
        elif result is False:
            logger.info("Test Case Failed for %s for %s", problem_name, test_input)
        else:
            logger.info("The result is %s", result)
