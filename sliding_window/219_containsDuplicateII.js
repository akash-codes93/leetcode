/**
 * https://leetcode.com/problems/contains-duplicate-ii/
 * @param nums
 * @param k
 * not a sliding window approach, used a auxiliary hashmap to store indices
 * time: O(n)
 * space: O(n)
 */

let containsNearbyDuplicate = function(nums, k) {
    let indexLocation = {}

    for(let i = 0; i < nums.length; i++){
        if (nums[i] in indexLocation && Math.abs(indexLocation[nums[i]] - i) <= k){
            return true
        }
        indexLocation[nums[i]] = i;
    }
    return false
};

o = containsNearbyDuplicate([1,2,3,1,2,3], k = 2)
console.log(o)
