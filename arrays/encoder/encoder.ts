import * as test from "node:test";

export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {

        const encoder = (toEncode:string[]): string=> {
            const messageLength = toEncode.map(mess => mess.length+'##').join('');
            const compressed = toEncode.join('');
            return messageLength+ compressed
        }

        const decoder = (encoded:string): string[]=> {
            const split = encoded.split("##");
            const message = split.pop();
            let prev = 0
            const decoded = split.map(len => {
                const curr = message.substring(prev, prev+Number(len))
                prev=Number(len)
                return curr
            })
            return decoded
        }

        const encoded = encoder(testInput);
        const decoded = decoder(encoded);
        console.log(decoded,testInput)

        return [testInput, decoded]
    }
}