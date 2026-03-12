export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: any) {
        const [matrix, n] = testInput;

        let included = 0;
        let excluded = 0;

        for (let i = 0; i < n; i++) {
            const current = Math.max(excluded, included);
            included = excluded + Math.max(matrix[0][i], matrix[1][i]);
            excluded = current;
        }

        return Math.max(excluded, included);
    }
}
