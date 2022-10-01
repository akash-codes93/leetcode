/**
 * https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
 *
 * ::Hard::
 * Two pointer
 * no prefix sum
 * T = O(n)
 * S = O(1)
 *
 */
let countSubarrays = function (nums, k) {
    let sum_till_now = 0;
    let l = 0;
    let r = 0;
    let cnt = 0

    while (l <= r && r < nums.length) {
        sum_till_now += nums[r]
        let score = sum_till_now * (r - l + 1)

        if (score < k) {
            cnt += (r - l + 1)
            r++;
        } else {
            sum_till_now -= nums[l]
            if (l !== r) {
                sum_till_now -= nums[r]
            }
            if (l === r) {
                l++;
                r++;
            } else {
                l++;
            }
        }
    }

    return cnt;
};

console.log(countSubarrays([2,1,4,3,5], 10))
console.log(countSubarrays([1,1,1], 5))
