export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        
        // The solution is the number of fibanacci series
        // Recursion with Memoization
        const cache = [];
        // const fib = (n) => {
        //     if(n<=2) {
        //         return n
        //     }
        //     if(cache[n] !== undefined) {
        //         return cache[n]
        //     }
        //     cache[n] = fib(n-1) + fib(n-2)
        //     console.log(cache)
        //     return cache[n]
        // }
        // return fib(testInput)

        // Iterative 
        const iterative = (n) => {
            if(n<=2){
                return n
            }
            let p1 = 1;
            let p2 = 2;

            for(let i=3; i<n+1; i++){
                const curr = p1 +p2;
                p1 = p2;
                p2 = curr;
            }
            return p2
        }
        return iterative(testInput)

    }
}