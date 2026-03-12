import * as test from 'node:test';

export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: any) {
        let maxVol: number = 0;

        let left = 0;
        let right = test.length;

        while (left < right) {
            const currMax =
                Math.min(testInput[left], testInput[right]) * (right - left);
            maxVol = Math.max(currMax, maxVol);
            if (testInput[left] < testInput[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxVol;
    }
}
