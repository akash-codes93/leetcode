/**
 * https://leetcode.com/problems/subarray-sums-divisible-by-k/
 * store remainder in prefix array
 * solution: https://www.youtube.com/watch?v=QM0klnvTQzk
 */

let subarraysDivByK = function(nums, k) {
    let prefixSum = {0: 1}
    let sum = 0
    let nice = 0

    for (let i = 0; i < nums.length; i++) {

        sum += nums[i]

        let remainder = sum % k

        // for handling negative cases
        if(remainder < 0){
            remainder = remainder + k
        }

        if (remainder in prefixSum) {
            nice += prefixSum[remainder]
            prefixSum[remainder]++;
        }
        else
            prefixSum[remainder] = 1
    }
    // console.log(prefixSum)
    return nice
};

// o = subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5)
// o = subarraysDivByK(nums = [5], k = 9)
o = subarraysDivByK([-1,2,9], 2)
console.log(o)