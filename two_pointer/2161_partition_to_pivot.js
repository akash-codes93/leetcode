/*
https://leetcode.com/problems/partition-array-according-to-given-pivot/
 */

let pivotArray = function (nums, pivot) {

    let partitioned_nums = [];

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < pivot) {
            partitioned_nums.push(nums[i])
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === pivot) {
            partitioned_nums.push(nums[i])
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > pivot) {
            partitioned_nums.push(nums[i])
        }
    }

    return partitioned_nums
};

o = pivotArray([9, 12, 5, 10, 14, 3, 10], 10)
console.log(o);