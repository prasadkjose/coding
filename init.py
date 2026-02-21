""" Entry module """ 

import logging
import sys
import os

# Param
# 1. Problem name

# Use problem name to
# 1. create a folder and .py and .ts file in it.
# 2. a test directory with a .py and .ts test files in it

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout # Directs log messages to standard output (console)
)

logger = logging.getLogger(__name__)
current_directory = os.getcwd()


def get_file_content(problem_name:str) -> str:
    """ Get the file context need to initilize python files
        The indendation looks weird so that the generated file will pass lint checks.
    """
    return f"""\"\"\" Solution Module \"\"\"
class Solution:
    \"\"\" Solution Module \"\"\"
    def {problem_name}(self):
         \"\"\" Solution Method \"\"\""""

def main():
    """
    Main method
    """
    input_problem_path = sys.argv[1]
    problem_name = input_problem_path

    if not os.path.exists(input_problem_path):
        logger.info("Creating a directory and code files.")
        os.makedirs(input_problem_path)
        path_arr = input_problem_path.split('/')
        code_file_path = ""
        if len(path_arr) == 1:
            code_file_path = current_directory+'/'+input_problem_path+'/'+input_problem_path
        else:
            code_file_path = current_directory+'/'+input_problem_path+'/'+path_arr[1]
            problem_name = path_arr[1]

        ts_file_init_content = ""

        # Add the content to the files
        try:
            with open(code_file_path + '.ts',"w", encoding="utf-8") as f:
                f.write(ts_file_init_content)
            with open(code_file_path + '.py',"w",  encoding="utf-8") as f:
                f.write(get_file_content(problem_name))
        except FileExistsError:
            logger.error("Files already exist")

        # Init Test files
        logger.info("Setting up test files.")
        test_file_path = current_directory+'/'+input_problem_path+'/test'
        os.makedirs(test_file_path)
        try:
            with open(test_file_path +"/test_" + problem_name  + '.py',"w", encoding="utf-8") as f:
                f.write("py_file_init_content")
        except FileExistsError:
            logger.error("Files already exist")

    else:
        logger.error('Try a new problem. This one already exists!')


main()
