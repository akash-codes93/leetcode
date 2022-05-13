/*
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
 */


let minPairSum = function(nums) {
    nums.sort((a, b) => a-b)
    let start = 0
    let end = nums.length-1
    let sum = 0

    while(start < nums.length/2){
        console.log("pairs: ",nums[start], nums[end]);
        let _sum = nums[start] + nums[end]
        if(_sum > sum){
            sum = _sum
        }
        start ++;
        end --;
    }
    return sum
};

o = minPairSum([3,5,4,2,4,6]);
console.log(o)