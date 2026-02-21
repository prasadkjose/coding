"""Testing Module"""
import logging
import importlib


logger = logging.getLogger(__name__)

class Test:
    """ Test Class """
    def test(self, solution_module_path):
        """Method to test solution"""
        # Example: arrays.contains_duplicate.contains_duplicate import Solution
        solution_module = importlib.import_module(solution_module_path)

        solution_class = solution_module.Solution()
        result = solution_class.run_solution()
        if result is True:
            logger.info("Test Passed")
        elif result is False:
            logger.error("Test Failed")
        else:
            logger.info("The result is %s", result)
