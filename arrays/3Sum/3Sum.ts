export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        const sorted: number[] = testInput.sort((a, b) => a - b);
        const result: number[][] = []
        
        for (let i =0; i<sorted.length; i++){
            let left = i+1;
            let right = sorted.length -1;

            while(left < right){
                const sum = sorted[i] + sorted[left] + sorted[right];

                if(sum>0) {
                    right--;
                } else if(sum<0){
                    left++;
                } else {
                    result.push([sorted[i], sorted[left], sorted[right]])
                    left++;
                    right++
                    while(left < right && sorted[left] === sorted[left -1]){
                        left++
                    }
                }
            }
        }
        return result
        console.log(sorted)
    }
}