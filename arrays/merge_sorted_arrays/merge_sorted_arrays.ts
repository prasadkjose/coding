export class Solution {
  /**
   * @param {string} testInput
   * @return {any} Returns either boolean to validate the test cases or a custom result.
   */
  run_solution(testInput: any) {
    const [nums1, nums2, m, n] = testInput;

    let i = m - 1;
    let j = n - 1;
    let right = n + m - 1;

    while (j >= 0) {
      if (i >= 0 && nums1[i] < nums2[j]) {
        nums1[right] = nums2[j];
        j--;
      } else {
        nums1[right] = nums1[i];
        i--;
      }
      right--;
    }
    return nums1;
  }
}
