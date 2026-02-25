export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any):[number, number] | undefined{
        const [nums, target] = testInput;
        const hashMap:Record<number,number> = {};
        let result 
        for(let idx=0; idx<nums.length; idx++) {
            const diff = target - nums[idx];
            const keys = Object.keys(hashMap)
            if(keys.includes(diff.toString())) {
                return [hashMap[diff], idx];
            }
            hashMap[nums[idx]] = idx;
        }
        return result
    }
}