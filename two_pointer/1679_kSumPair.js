/**
 * https://leetcode.com/problems/max-number-of-k-sum-pairs/
 */

let maxOperations = function (nums, k) {

    nums = nums.sort((a, b) => a - b)
    let i = 0;
    let j = nums.length-1;
    let count = 0;
    while (i < j) {

        if((nums[i]+ nums[j]) < k){
            i++;
        }
        else if ((nums[i]+ nums[j]) >k){
            j--;
        }
        else{
            count ++;
            i++;
            j--;
        }
    }

    return count
};

o = maxOperations(nums = [1,2,3,4], k = 5)
console.log(o);