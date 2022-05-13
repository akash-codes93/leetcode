/*
https://leetcode.com/problems/squares-of-a-sorted-array/
 */

let sortedSquares = function (nums) {
    let start_positive = 0;
    let start_negative = 0;
    let new_nums = [];

    while (nums[start_positive] < 0) {
        start_positive++;
    }

    start_negative = start_positive
    start_negative--;

    while (start_negative >= 0 || start_positive < nums.length) {
        if((nums[start_negative]**2 > nums[start_positive]**2) || start_negative < 0){
            new_nums.push(nums[start_positive]**2)
            start_positive++;
        }
        else{
            new_nums.push(nums[start_negative]**2)
            start_negative--;
        }
    }
    return new_nums
};

o = sortedSquares([-4,-2,1,2,3,4])
console.log(o)
