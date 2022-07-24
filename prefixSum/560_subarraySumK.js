/**
 * https://leetcode.com/problems/subarray-sum-equals-k/
 */

let subarraySum = function(nums, k) {
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

o = subarraySum(nums = [1,2,3], k = 3)
console.log(o);
