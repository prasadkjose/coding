class Test {
    /**
    * Test runner class. 
    * @param {string} problemName
    * @return {Promise<void>}
    */
    async test(problemName: string) {
        const solutionClassPath = `../${problemName}.ts`
        const { Solution } = await import(solutionClassPath);
        const solutionClass = new Solution()

        const testInput = 5
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
export {}