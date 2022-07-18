/**
 * https://leetcode.com/problems/max-consecutive-ones-iii/
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

let longestOnes = (nums, k) => {
    let i = 0;
    let j = 0;
    let max_len = 0;
    let current = 0

    while(j < nums.length && i <= j){

        if(nums[j] === 1){
            j ++;
            current ++
        }
        else if (nums[j] === 0 && k > 0){
            k--;
            current ++;
            j++;
        }
        else if(nums[i] === 1 && i < j){
            i+= 1
            current--;
        }
        else if(nums[i] === 0 && i < j){
            i ++;
            current --;
            k++;
        }
        if(i === j){
            i++;
            j++;
        }
        if(current > max_len){
            max_len = current
        }
    }

    return max_len;

};

// o = longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
o = longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1], k = 3)
// o = longestOnes(nums = [0,0,1,1,1,0,0], k = 0)
console.log(o);

