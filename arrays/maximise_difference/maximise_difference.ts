export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    // run_solution(testInput: any) {
    // //    [7,1,5,3,6,4] - Maximise difference - O(n)
    //     let maxProfit:number = 0
    //     let currentDiff:number = 0
    //     for(let idx = 0; idx<testInput.length; idx++) {
    //         const subArray = testInput.slice(idx+1)
    //         const current = testInput[idx]
    //         subArray.forEach(future => {
    //             currentDiff = future - current;
    //             maxProfit = Math.max(maxProfit, currentDiff)
    //         });
    //     }
    //     return maxProfit
    // }


    run_solution(testInput: any) {
    //    [7,1,5,3,6,4] - Maximise difference - and 
        let maxProfit = 0;
        let minSellPrice = 9999;
        for(let idx = 0; idx<testInput.length; idx++) {
            const todayprice = testInput[idx]
            if(todayprice < minSellPrice) {
                minSellPrice = todayprice;
            } else {
                const profit = todayprice - minSellPrice
                maxProfit = Math.max(maxProfit, profit)
            }
        
        }
        return maxProfit
    }
}