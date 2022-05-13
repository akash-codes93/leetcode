/*
https://leetcode.com/problems/rearrange-array-elements-by-sign/
 */

let rearrangeArray = function (nums) {
    let nums_positive = []
    let nums_negative = []

    nums.forEach(num => {
        if (num < 0) {
            nums_negative.push(num)
        } else {
            nums_positive.push(num)
        }
    })
    let positive_marker = 0;
    let negative_marker = 0

    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) {
            nums[i] = nums_positive[positive_marker]
            positive_marker++;
        } else {
            nums[i] = nums_negative[negative_marker]
            negative_marker++;
        }
    }
    return nums
};

const o = rearrangeArray([3,1,-2,-5,2,-4,])
console.log(o)