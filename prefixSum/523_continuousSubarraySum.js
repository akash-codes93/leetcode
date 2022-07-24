/**
 * https://leetcode.com/problems/continuous-subarray-sum/
 *
 * [23,2,4,6,6]
 * 7
 * I don't know how this is true
 */

let checkSubarraySum = function(nums, k) {
    let prefixSum = new Set();
    let sum = 0;
    let status = false

    for (let i = 0; i < nums.length; i++) {
        sum += nums[i]
        prefixSum.forEach (function(value) {
            console.log(sum, value, (sum - value));
            if((sum - value) % k === 0){
                console.log("I am here!")
                status = true
            }

        })
        if (!(sum in prefixSum))
            prefixSum.add(sum);
    }
    // console.log(prefixSum)
    return status
};

o = checkSubarraySum(nums = [23,2,4,6,6], k = 7)
console.log(o)


