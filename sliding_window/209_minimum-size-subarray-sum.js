/**
 * https://leetcode.com/problems/minimum-size-subarray-sum/
 * it's a class two pointer question
 */


let minSubArrayLen = function (target, nums) {

    let l = 0;
    let r = 0;
    let total_sub_sum = 0;
    let min_count = 9999999999;

    while (l <= r && r < nums.length) {
        total_sub_sum += nums[r];

        if (total_sub_sum >= target) {
            let len = r - l + 1;
            if (min_count > len) {
                min_count = len;
            }
            total_sub_sum -= nums[l]
            total_sub_sum -= nums[r]
            l++;
        } else {
            r++;
        }
    }
    if(min_count === 9999999999) {
        return 0
    }
    return min_count
};


// console.log(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
// console.log(minSubArrayLen(target = 4, nums = [1,4,4]))
console.log(minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))

