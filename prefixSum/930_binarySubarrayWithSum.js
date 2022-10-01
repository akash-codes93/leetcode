/**
 * https://leetcode.com/problems/binary-subarrays-with-sum/
 * Same as 560
 *
 */
let numSubarraysWithSum = function (nums, goal) {
    let sum_map = {0: 1};
    let count = 0;
    let sum_till_now = 0;

    for (let i = 0; i < nums.length; i++) {
        sum_till_now += nums[i];
        let req_sum = sum_till_now - goal;

        if (req_sum in sum_map) {
            count += sum_map[req_sum];
        }

        if (sum_till_now in sum_map) {
            sum_map[sum_till_now] += 1
        } else{
            sum_map[sum_till_now] = 1
        }
    }
    return count;
};

console.log(numSubarraysWithSum([1,0,1,0,1], 2))
