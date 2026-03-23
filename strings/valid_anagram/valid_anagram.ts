export class Solution {
    /**
     * @param {string} testInput
     * @return {any} Returns either boolean to validate the test cases or a custom result.
     */
    run_solution(testInput: string[]) {
        const [s, t] = testInput;
        const hashMap: Record<string, number> = {};
        s.split('').forEach(char => {
            if (char in hashMap) {
                hashMap[char]++;
            } else {
                hashMap[char] = 1;
            }
        });

        t.split('').forEach(char => {
            if (char in hashMap) {
                hashMap[char]--;
            } else {
                hashMap[char] = undefined;
            }
        });
        console.log(Object.values(hashMap));
    }
}
