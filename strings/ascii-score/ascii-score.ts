export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: string) {
        const stringArr = testInput.split('');

        return stringArr.reduce((acc, curr, idx) => {
            if (idx === stringArr.length - 1) return acc;
            return (
                acc +
                Math.abs(stringArr[idx + 1].charCodeAt(0) - curr.charCodeAt(0))
            );
        }, 0);
    }
}
