import { hash } from "node:crypto";
import * as test from "node:test";

export class Solution {
    /**
    * @param {string} testInput
    * @return {any} Returns either boolean to validate the test cases or a custom result. 
    */
    run_solution(testInput: any) {
        // Input: strs = ["act","pots","tops","cat","stop","hat"]
        // Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        const hashMap: Record<string, [string]> = {};
        
        testInput.forEach(element => {
            const sorted = element.split("").sort().join("");;
            if(hashMap[sorted]) {
                hashMap[sorted].push(element);
            } else {
                hashMap[sorted] = [element]
            }
        });
        return Object.values(hashMap)
    }
}