/**
 * https://leetcode.com/problems/maximum-average-subarray-i/
 */

let findMaxAverage = (nums, k) => {

    let i = 0, j = k - 1, max_average = 0, sum = 0;
    for (let p = i; p <= j; p++) {
        sum += nums[p]
    }

    while (j < nums.length) {


        let avg_ = sum / k

        if (avg_ > max_average)
            max_average = avg_

        sum -= nums[i];

        i++;
        j++;
        sum += nums[j]

    }

    return max_average

};

o = findMaxAverage(nums = [1, 12, -5, -6, 50, 3], k = 4)
console.log(o);

