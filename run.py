""" Entry module """ 

import logging
import sys
import os
import importlib
import subprocess

from utils.generator import Generator

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout # Directs log messages to standard output (console)
)

logger = logging.getLogger(__name__)
current_directory = os.getcwd()

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
            generator = Generator()

            logger.info("Creating a directory and code files.")
            os.makedirs(solution_file_path)

            # Add the content to the files
            try:
                with open(code_file_name + '.ts',"w", encoding="utf-8") as f:
                    f.write(generator.get_and_generate_files('TypeScript', False))
                with open(code_file_name + '.py',"w",  encoding="utf-8") as f:
                    f.write(generator.get_and_generate_files('Python',False))
            except FileExistsError:
                logger.error("Files already exist")
            except SystemExit:
                logger.error("Need to provide a programming language")


            # Init Test files
            logger.info("Setting up test files.")
            os.makedirs(test_file_path)
            try:
                with open(test_file_name+ '.py',"w", encoding="utf-8") as f:
                    f.write(generator.get_and_generate_files('Python', True))
                with open(test_file_name+ '.ts',"w", encoding="utf-8") as f:
                    f.write(generator.get_and_generate_files('TypeScript', True))
            except FileExistsError:
                logger.error("Files already exist")
            except SystemExit:
                logger.error("Need to provide a programming language")

        else:
            logger.error('Try a new problem. This one already exists!')

    elif mode == "test":
    
        # PYTHON
        # Example: from arrays.contains_duplicate.test.test_contains_duplicate import Test
        test_module_path = relative_test_file_name.replace("/",".")
        solution_module_path = relative_solution_file_path.replace("/",".")
        logger.info("Running Python Test module from %s",test_module_path)

        test_module = importlib.import_module(test_module_path)
        test_class = test_module.Test()
        test_class.test(solution_module_path, problem_name)
        print(problem_name)
        # TypeScript
        logger.info("Running TypeScript Test module")
        result = subprocess.run(
        ["npx", "ts-node", relative_test_file_name+".ts", problem_name],
        capture_output=True,
        text=True,
        check=False
        )

        if result.returncode == 0:
            print("Success:", result.stdout)
        else:
            print("Error:", result.stderr)


    else:
        logger.error("You can either \"init\" or \"test\" your solutions")


main()
