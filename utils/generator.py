""" Utility module that generates code templates."""
import logging
import sys

logger = logging.getLogger(__name__)

class Generator:
    """Class to generate language specific templates."""

    def _generate_python_files(self, is_test)->str:
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

    def _generate_typescript_files(self, is_test)->str:
        """ Method to generate TypeScript files """ 
        if is_test is True:
            return """class Test {
    /**
    * Test runner class. 
    * @param {string} problemName
    * @return {Promise<void>}
    */
    async test(problemName: string) {
        const solutionClassPath = `../${problemName}.ts`
        const { Solution } = await import(solutionClassPath);
        const solutionClass = new Solution()

        const testInput = []
        const result = solutionClass.run_solution(testInput)
        if(result === true) {
            console.log(`Test Case Passed for ${problemName} for ${testInput}`)
        } else if(result === false) {
            console.log(`Test Case Failed for ${problemName} for ${testInput}`)
        } else {
            console.log(`The result is ${result}`)
        }
    }
}

const testObj: Test = new Test()
// Get the command line args needed to run the test.
const problemName = process.argv[2]
await testObj.test(problemName)

// Export an empty module to run the code asynchronously. 
export {}"""

        return """export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        return true
    }
}"""


    def get_and_generate_files(self, language: str, is_test: bool)->str:
        """ Determine the language and return the necessary template"""
        if language == 'Python':
            return self._generate_python_files(is_test)
        if language == 'TypeScript':
            return self._generate_typescript_files(is_test)
        return sys.exit("Need to provide a programming language")
