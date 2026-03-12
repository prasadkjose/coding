export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: any) {
        let [nums, k] = testInput;
        k = k % nums.length;

        if (k != 0) {
            const temp = nums.slice(-k).concat(nums.slice(0, k + 1));
            nums = temp;
        }
        return nums;
    }
}
