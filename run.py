""" Entry module """ 

import logging
import sys
import os
import importlib


# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout # Directs log messages to standard output (console)
)

logger = logging.getLogger(__name__)
current_directory = os.getcwd()


def get_file_content(problem_name:str, is_test:bool) -> str:
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
    def test(self, solution_module_path):
        \"\"\"Method to test solution\"\"\"
        # Example: arrays.contains_duplicate.contains_duplicate import Solution
        solution_module = importlib.import_module(solution_module_path)

        solution_class = solution_module.Solution()
        result = solution_class.run_solution()
        if result is True:
            logger.info("Test Passed")
        elif result is False:
            logger.error("Test Failed")
        else:
            logger.info("The result is %s", result)"""


    return """\"\"\" Solution Module \"\"\"
class Solution:
    \"\"\" Solution Module \"\"\"
    def run_solution(self):
        \"\"\" Solution Method \"\"\"
        return True"""

def main():
    """
    Main method
    """

    # Argument Parsing
    mode = sys.argv[1]
    solution_file_path = sys.argv[2]
    problem_name = solution_file_path

    # File Path Parsing - Both relative from entry and from home dir.
    path_arr = solution_file_path.split('/')
    code_file_path = current_directory+'/'+solution_file_path
    relative_solution_file_path = solution_file_path

    if len(path_arr) == 1:
        code_file_name = code_file_path+'/'+solution_file_path
        relative_solution_file_path = relative_solution_file_path +'/'+solution_file_path
    else:
        problem_name = path_arr[1]
        code_file_name = code_file_path+'/'+problem_name
        relative_solution_file_path = relative_solution_file_path +'/'+problem_name

    test_file_path = current_directory+'/'+solution_file_path+'/test'
    test_file_name = test_file_path +"/test_" + problem_name

    relative_test_file_path = solution_file_path+'/test'
    relative_test_file_name = relative_test_file_path +"/test_" + problem_name

    if mode == "init":
        if not os.path.exists(solution_file_path):
            logger.info("Creating a directory and code files.")
            os.makedirs(solution_file_path)

            ts_file_init_content = ""

            # Add the content to the files
            try:
                with open(code_file_name + '.ts',"w", encoding="utf-8") as f:
                    f.write(ts_file_init_content)
                with open(code_file_name + '.py',"w",  encoding="utf-8") as f:
                    f.write(get_file_content(problem_name, False))
            except FileExistsError:
                logger.error("Files already exist")

            # Init Test files
            logger.info("Setting up test files.")
            os.makedirs(test_file_path)
            try:
                with open(test_file_name+ '.py',"w", encoding="utf-8") as f:
                    f.write(get_file_content(problem_name, True))
            except FileExistsError:
                logger.error("Files already exist")

        else:
            logger.error('Try a new problem. This one already exists!')

    elif mode == "test":
        test_module_path = relative_test_file_name.replace("/",".")
        solution_module_path = relative_solution_file_path.replace("/",".")
        logger.info("Running Test module from %s",test_module_path)
        # Example: from arrays.contains_duplicate.test.test_contains_duplicate import Test
        test_module = importlib.import_module(test_module_path)
        test_class = test_module.Test()
        test_class.test(solution_module_path)

    else:
        logger.error("You can either \"init\" or \"test\" your solutions")


main()
