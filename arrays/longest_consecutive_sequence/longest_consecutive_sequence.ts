export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: number[]) {
        const sorted:number[] = [...new Set(testInput.sort((a, b) => a - b))]
        let longest = 1;
        let currSequence = 1
        if(testInput.length === 0) {
            return 0
        }
        sorted.forEach((num,i) => {
            if(num-sorted[i-1] ===1) {
                currSequence++
            } else {
                currSequence = 1
            }
            longest = Math.max(longest, currSequence)
        })
    

        return longest
    }
}