export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: any) {
        const [nums, k] = testInput;
        const sorted = nums.sort((a, b) => a - b);
        return sorted[k - 1];
    }
}
