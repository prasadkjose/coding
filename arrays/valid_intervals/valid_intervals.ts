export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        // Sort the arrays by start times. 
        const startTimes: number[] = testInput.map(arr => arr[0]);
        const sortedStart: number[] = startTimes.sort()
        let isValid: boolean = true

        testInput.forEach((currentInterval:number, idx:number) => {
            const currentEnd: number = currentInterval[1];
            if(currentEnd > sortedStart[idx +1]){
                isValid = false
            }
            
        });
        return isValid
    }
}