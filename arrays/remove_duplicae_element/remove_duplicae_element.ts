export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: any) {
        let k = 2;
        let i = 2;
        for (; i < testInput.length; i++) {
            if (testInput[i] !== testInput[k - 2]) {
                testInput[k] = testInput[i];
                k++;
            }
        }
        return k;
    }
}
