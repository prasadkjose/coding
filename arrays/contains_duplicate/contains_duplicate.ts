export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: number[]) {
        const set = new Set(testInput);
        return set.size !== testInput.length;
    }
}
