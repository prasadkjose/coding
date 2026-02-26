export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        // nums = [1,2,2,3,3,3], k = 2
        const [nums, k] = testInput;
        const mapObj = {};
        const result = [];
        nums.forEach(element => {
            if(mapObj[String(element)]) {
                mapObj[String(element)]++
            } else {
                mapObj[String(element)] = 1
            }
            if(mapObj[String(element)] >= k) {
                result.push(element)
            }
        });
        return [...new Set(result)]
    }
}