export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        // "()"
        // "("
        const toCheck: string[] = testInput.split('');
        const stacked: string[] = [];
        const valid: Record<string, string> = {
            '[': '{',
            ']': '[',
            ')': '('
        }
        for(let i=0; i<toCheck.length; i++) {
            const current = toCheck[i];
            const stackTop = stacked.at(-1)
            if(stacked.length === 0) {
                stacked.push(current)
            } else if(stackTop === valid[current]) {
                stacked.pop();
            } else {
                stacked.push(current)
            }
            
        }
        return !stacked.length
    }
}