/*
https://leetcode.com/problems/sort-array-by-parity-ii/
 */

let sortArrayByParityII = function (nums) {
    let even = 0;
    let odd = 1;

    while (even < nums.length && odd < nums.length) {

        if (nums[even] % 2 !== 0 && nums[odd] % 2 === 0) {
            let p = nums[even];
            nums[even] = nums[odd];
            nums[odd] = p;
        }
        if (nums[even] % 2 === 0){
            even += 2
        }
        if (nums[odd] % 2 !== 0){
            odd += 2
        }
    }
    return nums
};

o = sortArrayByParityII([3,2])
console.log(o);