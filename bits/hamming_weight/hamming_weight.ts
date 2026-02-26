export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        //  Hamming  weight or population count is the number of 1s in an binary rep of a number. 
        let count = 0;
        for(let i=0; i<32; i++){
            console.log(testInput)
            if((1 << i) & testInput) {
                count++; 
            }
        }
        return count; 
    }
}