/**
 * https://leetcode.com/problems/binary-subarrays-with-sum/
 * same as 560, 1248
 */

var numSubarraysWithSum = function(nums, k) {
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

o = numSubarraysWithSum(nums = [1,0,1,0,1], k = 2)
console.log(o)
