/*
https://leetcode.com/problems/make-sum-divisible-by-p/
solution:
remainder of full arr  sum = 5
now find sub array sum with 5
and store last index in hash map
 */

let MAX_LEN = 999999

let minSubarray = function (nums, p) {

    let total_sum = nums.reduce((a, b) => a + b, 0)
    if (total_sum % p === 0) {
        return 0
    } else if (total_sum < p) {
        return -1
    }

    let sum = total_sum % p;
    let hash_map = {0: -1};
    let min_len = MAX_LEN
    let sum_till_now = 0;
    for (let i = 0; i < nums.length; i++) {
        sum_till_now += nums[i];

        let remainder_sum = (sum_till_now - sum) % p  // % p part is extra 5-5 = 0 x-5 % p = 0 is same

        if (remainder_sum in hash_map) {
            let len = i - hash_map[remainder_sum]

            if (len < min_len) {
                min_len = len
            }


        }
        hash_map[sum_till_now % p] = i
    }

    if (min_len === MAX_LEN) {
        return -1
    } else if (min_len === nums.length) {
        return -1
    }
    return min_len

};

console.log(minSubarray([3,2,1,4,5,0,2], 6))
console.log(minSubarray([6,3,5,2], 9))
console.log(minSubarray([6,2], 9))
console.log(minSubarray([5,9], 13))
console.log(minSubarray([4,9], 13))
console.log(minSubarray([26, 19, 11, 14, 18, 4, 7, 1, 30, 23, 19, 8, 10, 6, 26, 3], 26))
console.log(minSubarray([4,4,2], 7))

