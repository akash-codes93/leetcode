/*
https://leetcode.com/problems/sort-array-by-parity/
 */

let sortArrayByParity = function (nums) {
    let min_odd = 0;
    let nums_len = nums.length;
    let max_even = nums_len - 1;


    while (max_even > min_odd) {
        if (nums[max_even] % 2 !== 0) {
            max_even--;
        } else if (nums[min_odd] % 2 === 0) {
            min_odd++;
        } else {
            let k = nums[min_odd]
            nums[min_odd] = nums[max_even]
            nums[max_even] = k
            min_odd++;
            max_even--;
        }
    }

    return nums
};

// const o = sortArrayByParity([2, 4, 3, 1, 6])
// const o = sortArrayByParity([1, 3, 5, 6, 8, 2, 7, 4, 1])
const o = sortArrayByParity([0])
console.log(o)