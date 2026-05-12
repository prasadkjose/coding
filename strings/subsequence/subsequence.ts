export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: string[]) {
        const [s, t] = testInput;
        let i = 0;
        let j = 0;

        while (i < s.length && j < t.length) {
            if (s[i] === t[j]) {
                j++;
            }
            i++;
        }

        return t.length - j;
    }
}
