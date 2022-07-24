/**
 * https://leetcode.com/problems/count-number-of-nice-subarrays/
 * convert array to 0 & 1
 * problem changes to subarrays with sum K
 * use prefixsum approach on it
 * https://www.youtube.com/watch?v=fFVZt-6sgyo
 */

let numberOfSubarrays = function (nums, k) {


    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % 2 === 0) {
            nums[i] = 0;
        }
    }

    let prefixSum = {0: 1}
    let sum = 0
    let nice = 0

    for (let i = 0; i < nums.length; i++) {

        sum += nums[i]
        let required_sum = sum - k

        if (required_sum in prefixSum) {
            nice += prefixSum[required_sum]
        }

        if (sum in prefixSum)
            prefixSum[sum]++;
        else
            prefixSum[sum] = 1
    }
    // console.log(prefixSum)
    return nice
};

o = numberOfSubarrays(nums = [1, 1, 2, 1, 1], k = 3)
// o = numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k = 2)
console.log(o);