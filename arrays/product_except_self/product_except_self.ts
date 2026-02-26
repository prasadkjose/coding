export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        // [1,2,4,6]
        // [1, 1, 2, 8]
        // [1,1,2,8]
        // [48, 24, 12, 8]
        const length = testInput.length
        const result = [length].fill(1)

        let suffix = 1;
        for(let i =1; i<length;i++){
            result[i] = result[i-1] * testInput[i-1];
        }
        for(let i=length-1; i>=0; i-- ) {
            result[i] = result[i] * suffix
            suffix = suffix * testInput[i];
        }
        return result
    }
}