import * as test from "node:test"

export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        const result = testInput + testInput
        console.log(result)
        return result
    }
}