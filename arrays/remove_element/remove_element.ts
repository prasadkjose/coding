export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: any) {
        const [nums, val] = testInput;

        let k = 0;

        nums.forEach(e => {
            if (e !== val) {
                nums[k] = e;
                k++;
            }
        });

        return nums;
    }
}
